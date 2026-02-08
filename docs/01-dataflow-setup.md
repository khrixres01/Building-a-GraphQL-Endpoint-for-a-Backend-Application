
# 01 — Dataflow Setup (Curated Table)

This step documents creating a **Dataflow Gen2** that produces a curated table from an existing source table, including filters to expose only the fields/rows required by developers.

## Steps (high level)
1. In Fabric → **Data Factory → Dataflows Gen2** → *New Dataflow*.
2. Add source tables (e.g., Lakehouse/Warehouse).
3. Apply **Filter**/**Select columns** transformations to keep only required data.
4. **Output** to Lakehouse table (e.g., `ab_e_merged`).
5. Save the dataflow.

> Tip: Prefer exposing **views/materialized views** to keep API semantics stable for downstream apps.
