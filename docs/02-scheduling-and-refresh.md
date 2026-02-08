
# 02 — Scheduling & Refresh

Configure a scheduled refresh on the dataflow so the curated table stays up to date.

## Steps
1. Open the dataflow → **Schedule**.
2. Set frequency and time zone (e.g., hourly at :15).
3. (Optional) Configure incremental refresh if supported.
4. Validate in **Monitoring** and set alerts.

## Notes
- Align refresh with upstream ingestion windows.
- Document SLAs and latency expectations for consumers.
