
# 04 — Service Principal Authentication (Client Credentials)

Use **Microsoft Entra ID** OAuth 2.0 **client credentials** (app‑only) to get tokens.

## Token endpoint (v2)
```
POST https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token
```

### Headers
```
Content-Type: application/x-www-form-urlencoded
```

### Body
```
grant_type=client_credentials
client_id=<CLIENT_ID>
client_secret=<CLIENT_SECRET>
scope=https://api.fabric.microsoft.com/.default
```

Store all values in a local `.env` file (never commit to Git).
