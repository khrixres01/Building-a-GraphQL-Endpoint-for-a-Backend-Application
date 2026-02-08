
# 06 — Postman Guide (Manual, Non‑Interactive)

## Token request
- **URL:** `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token`
- **Method:** `POST`
- **Headers:** `Content-Type: application/x-www-form-urlencoded`
- **Body (x-www-form-urlencoded):**
  - `grant_type=client_credentials`
  - `client_id=<CLIENT_ID>`
  - `client_secret=<CLIENT_SECRET>`
  - `scope=https://api.fabric.microsoft.com/.default`

## GraphQL request
- **URL:** `<FABRIC_GRAPHQL_ENDPOINT>`
- **Method:** `POST`
- **Headers:**
  - `Authorization: Bearer <ACCESS_TOKEN>`
  - `Content-Type: application/json`
- **Body:** GraphQL query JSON

> Do not use interactive OAuth helpers; keep headers minimal.
