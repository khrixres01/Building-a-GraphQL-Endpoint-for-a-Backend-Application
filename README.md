# Building-a-GraphQL-Endpoint-for-a-Backend-Application
A practical guide to create a Microsoft Fabric Graphql Endpoint from a dataflow Gen2 table 

# Fabric GraphQL Delivery (Dataflow + GraphQL + SP + Python)

This repository documents and demonstrates the setup for:
- Curating data with **Dataflow Gen2** (filters + scheduled refresh)
- Exposing curated data via **Microsoft Fabric API for GraphQL**
- Authenticating with **Service Principal** (OAuth 2.0 client credentials)
- Testing the GraphQL endpoint from **Python** and **Postman**

> **Security first:** never commit secrets. Use `.env` locally; commit only `.env.example`.

## Quick start

1. **Clone** and prepare environment variables:
   ```bash
   git clone <YOUR_REPO_URL>
   cd fabric-graphql-delivery
   cp .env.example .env   # fill in local values (never commit .env)
   ```

2. **Python demo** (optional):
   ```bash
   cd examples/python
   python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   python client.py
   ```

3. **Postman demo** (optional):
   - Import `examples/postman/Fabric_GraphQL.postman_collection.json`
   - Create a Postman **Environment** with keys:
     - `TENANT_ID`, `CLIENT_ID`, `CLIENT_SECRET`, `FABRIC_GRAPHQL_ENDPOINT`
   - Run **Get Token** (form‑urlencoded), then **GraphQL Query** (Bearer token).

## Documentation
- docs/01-dataflow-setup.md
- docs/02-scheduling-and-refresh.md
- docs/03-graphql-api-setup.md
- docs/04-service-principal-auth.md
- docs/05-testing-with-python.md
- docs/06-postman-guide.md
- docs/07-troubleshooting.md

## License & security
- See `LICENSE` and `SECURITY.md`.

