
import os, json
import requests
from urllib.parse import urlencode

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass  # dotenv is optional if environment variables are already present

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
GRAPHQL_ENDPOINT = os.getenv("FABRIC_GRAPHQL_ENDPOINT")
TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))

if not all([TENANT_ID, CLIENT_ID, CLIENT_SECRET, GRAPHQL_ENDPOINT]):
    raise RuntimeError("Missing required environment variables. Check your .env file.")

# 1) Acquire token
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
body = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": "https://api.fabric.microsoft.com/.default",
}
headers = {"Content-Type": "application/x-www-form-urlencoded"}

resp = requests.post(TOKEN_URL, data=urlencode(body), headers=headers, timeout=TIMEOUT)
resp.raise_for_status()
access_token = resp.json().get("access_token")
if not access_token:
    raise RuntimeError(f"Token acquisition failed: {resp.text}")

# 2) GraphQL query
query = {
    "query": """
        query ($first:Int!) {
          kTNL_Outputts(first:$first) {
            items { BWART MATNR WERKS MENGE }
          }
        }
    """,
    "variables": {"first": 10},
}

gql_headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

r = requests.post(GRAPHQL_ENDPOINT, json=query, headers=gql_headers, timeout=TIMEOUT)
print("Status:", r.status_code)
try:
    print(json.dumps(r.json(), indent=2))
except Exception:
    print("Raw response:
", r.text)
