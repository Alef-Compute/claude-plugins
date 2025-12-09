#!/usr/bin/env python3
"""
Reducto Document Converter

Converts PDF and DOCX files to Markdown using the Reducto API.
Used by the document-ingest skill for contract review workflows.

Usage:
    python reducto_convert.py <input_file> <output_file>

Environment:
    REDUCTO_API_KEY - Your Reducto API key (required)

Example:
    python reducto_convert.py contract.pdf contract.md
"""

import os
import sys
import json
import requests
from pathlib import Path


REDUCTO_BASE_URL = "https://platform.reducto.ai"
REDUCTO_UPLOAD_URL = f"{REDUCTO_BASE_URL}/upload"
REDUCTO_PARSE_URL = f"{REDUCTO_BASE_URL}/parse"


def get_api_key():
    """Get Reducto API key from environment."""
    api_key = os.environ.get("REDUCTO_API_KEY")
    if not api_key:
        print("Error: REDUCTO_API_KEY environment variable not set.", file=sys.stderr)
        print("\nTo set it:", file=sys.stderr)
        print("  export REDUCTO_API_KEY='your-api-key-here'", file=sys.stderr)
        print("\nGet your API key at: https://reducto.ai", file=sys.stderr)
        sys.exit(1)
    return api_key


def upload_file(file_path: Path, api_key: str) -> str:
    """
    Upload a file to Reducto and get the file URL.
    
    Args:
        file_path: Path to the file to upload
        api_key: Reducto API key
        
    Returns:
        The file URL to use in parse request
    """
    print(f"Uploading file to Reducto...")
    
    with open(file_path, 'rb') as f:
        files = {
            'file': (file_path.name, f, 'application/octet-stream')
        }
        headers = {
            'Authorization': f'Bearer {api_key}'
        }
        
        response = requests.post(
            REDUCTO_UPLOAD_URL,
            headers=headers,
            files=files,
            timeout=120
        )
    
    if response.status_code != 200:
        raise Exception(f"Upload failed with status {response.status_code}: {response.text}")
    
    result = response.json()
    
    # The response should contain a file_url or similar
    file_url = result.get('file_url') or result.get('url') or result.get('file_id')
    
    if not file_url:
        # If we get a presigned URL response, the file_url might be in a different format
        if 'presigned_url' in result:
            file_url = result['presigned_url']
        else:
            raise Exception(f"Could not get file URL from upload response: {result}")
    
    print(f"File uploaded successfully.")
    return file_url


def parse_document(file_url: str, api_key: str) -> dict:
    """
    Parse an uploaded document using Reducto API.
    
    Args:
        file_url: The URL of the uploaded file
        api_key: Reducto API key
        
    Returns:
        The API response containing parsed content
    """
    print(f"Parsing document...")
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'document_url': file_url,
        'options': {
            'chunking': {
                'enabled': False
            },
            'table_output_format': 'md'
        }
    }
    
    response = requests.post(
        REDUCTO_PARSE_URL,
        headers=headers,
        json=payload,
        timeout=300
    )
    
    if response.status_code != 200:
        raise Exception(f"Parse failed with status {response.status_code}: {response.text}")
    
    return response.json()


def convert_document(input_path: str, output_path: str) -> bool:
    """
    Convert a PDF or DOCX file to Markdown using Reducto API.
    
    Args:
        input_path: Path to the input file (PDF or DOCX)
        output_path: Path for the output Markdown file
        
    Returns:
        True if conversion succeeded, False otherwise
    """
    input_file = Path(input_path)
    output_file = Path(output_path)
    
    if not input_file.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        return False
    
    supported_extensions = {'.pdf', '.docx', '.doc'}
    if input_file.suffix.lower() not in supported_extensions:
        print(f"Error: Unsupported file type: {input_file.suffix}", file=sys.stderr)
        print(f"Supported types: {', '.join(supported_extensions)}", file=sys.stderr)
        return False
    
    api_key = get_api_key()
    
    print(f"Converting: {input_file.name}")
    print(f"Using Reducto API...")
    
    try:
        # Step 1: Upload the file
        file_url = upload_file(input_file, api_key)
        
        # Step 2: Parse the document
        result = parse_document(file_url, api_key)
        
        # Step 3: Extract markdown
        markdown_content = extract_markdown(result)
        
        if not markdown_content:
            print("Error: No content extracted from document", file=sys.stderr)
            print(f"API Response: {json.dumps(result, indent=2)[:1000]}", file=sys.stderr)
            return False
        
        # Step 4: Save output
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"Success! Output saved to: {output_path}")
        return True
        
    except requests.exceptions.Timeout:
        print("Error: Request timed out. The document may be too large.", file=sys.stderr)
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error: Network request failed: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return False


def extract_markdown(api_response: dict) -> str:
    """
    Extract markdown content from Reducto API response.
    
    Args:
        api_response: The JSON response from Reducto API
        
    Returns:
        Markdown string or empty string if extraction fails
    """
    try:
        # Check for chunks in result
        if 'result' in api_response:
            result = api_response['result']
            
            # If result has chunks, extract content from them
            if isinstance(result, dict) and 'chunks' in result:
                chunks = result['chunks']
                if chunks and len(chunks) > 0:
                    # Get content from all chunks
                    contents = []
                    for chunk in chunks:
                        if isinstance(chunk, dict):
                            content = chunk.get('content') or chunk.get('text') or chunk.get('markdown', '')
                            if content:
                                contents.append(content)
                    if contents:
                        return '\n\n'.join(contents)
            
            # Direct string result
            if isinstance(result, str):
                return result
            
            # Dict with direct content
            if isinstance(result, dict):
                if 'markdown' in result:
                    return result['markdown']
                if 'content' in result:
                    return result['content']
                if 'text' in result:
                    return result['text']
            
            # List of blocks
            if isinstance(result, list):
                blocks = []
                for block in result:
                    if isinstance(block, dict):
                        content = block.get('content') or block.get('text') or block.get('markdown', '')
                        if content:
                            blocks.append(content)
                    elif isinstance(block, str):
                        blocks.append(block)
                return '\n\n'.join(blocks)
        
        # Top-level content fields
        if 'markdown' in api_response:
            return api_response['markdown']
        if 'content' in api_response:
            return api_response['content']
        if 'text' in api_response:
            return api_response['text']
        
        # Check for chunks at top level
        if 'chunks' in api_response:
            chunks = api_response['chunks']
            contents = []
            for chunk in chunks:
                if isinstance(chunk, dict):
                    content = chunk.get('content') or chunk.get('text') or chunk.get('markdown', '')
                    if content:
                        contents.append(content)
            if contents:
                return '\n\n'.join(contents)
            
    except Exception as e:
        print(f"Warning: Error extracting markdown: {e}", file=sys.stderr)
    
    return ""


def main():
    if len(sys.argv) != 3:
        print("Usage: python reducto_convert.py <input_file> <output_file>")
        print("\nExample:")
        print("  python reducto_convert.py contract.pdf contract.md")
        print("  python reducto_convert.py agreement.docx agreement.md")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    success = convert_document(input_path, output_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
