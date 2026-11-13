import os
import json
import requests
import sys

def fetch_manifest():
    token = os.getenv("GITHUB_TOKEN")
    owner = os.getenv("REPO_OWNER", "aws")
    repo = os.getenv("REPO_NAME", "aws-emulator-evaluation-suite")
    
    # Using the raw content URL to get the manifest.jsonl
    # Note: If no token is provided, rate limits may apply
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/manifest.jsonl"
    
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    print(f"Fetching manifest from {url}...")
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching manifest: {e}")
        sys.exit(1)

def main():
    manifest_data = fetch_manifest()
    lines = manifest_data.strip().split('\n')
    
    print(f"{'CHECK_ID':<60} | {'SERVICE':<15} | {'OPERATIONS'}")
    print("-" * 100)

    count = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            data = json.loads(line)
            check_id = data.get("check_id", "unknown")
            service = data.get("service", "unknown")
            ops = ", ".join(data.get("operations", []))
            
            print(f"{check_id[:58]:<60} | {service:<15} | {ops}")
            count += 1
        except json.JSONDecodeError:
            continue

    print("-" * 100)
    print(f"Total behaviors identified: {count}")

if __name__ == "__main__":
    main()
