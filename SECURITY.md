
# Security Policy

- **Never commit secrets** (client secrets, tokens, certificates). Use `.env` locally.
- Rotate the Service Principal secret or certificates if exposure is suspected.
- Store secrets in a secure vault (e.g., Azure Key Vault) and/or CI secrets store.
- Report security issues privately to your security contact.
