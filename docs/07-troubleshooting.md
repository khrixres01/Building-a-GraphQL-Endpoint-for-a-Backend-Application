
# 07 — Troubleshooting

- **AADSTS90013 / HTML login page**: Wrong token request (use v2 endpoint, form‑urlencoded body, `.default` scope). Do not send browser headers.
- **Bad Request – Invalid Hostname**: Check the exact URL; remove any manual `Host` header.
- **401**: Expired or missing token; acquire a fresh token.
- **403**: Service Principal lacks permissions on the workspace/API/data.
- **GraphQL `errors[]`**: Query uses fields not present in the schema or missing variables.
