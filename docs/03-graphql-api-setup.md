
# 03 — Fabric GraphQL API Setup

Expose the curated table via **API for GraphQL** in Fabric.

## Steps
1. In the Fabric workspace, create an **API for GraphQL** item.
2. Click **Get data** and select the curated table/view(s) to expose.
3. Confirm the generated schema in **Schema explorer**.
4. (Optional) **Export schema** to share with developers.

## Endpoint
```
POST https://<region>.graphql.fabric.microsoft.com/v1/workspaces/<workspace-id>/graphqlapis/<api-id>/graphql
```

Keep this URL in an environment variable; do not hardcode in code or docs.
