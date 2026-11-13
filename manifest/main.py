import os
import requests
import sys

def main():
    owner = os.getenv("REPO_OWNER", "aws")
    repo = os.getenv("REPO_NAME", "aws-emulator-evaluation-suite")
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/manifest.jsonl"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Stream the content directly to stdout
        sys.stdout.write(response.text)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

