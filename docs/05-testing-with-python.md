
# 05 — Testing with Python

A minimal Python client is included under `examples/python/`.

## Run locally
```bash
cd examples/python
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp ../../.env.example ../../.env  # if not created yet, then fill real values
python client.py
```

Expected output: HTTP status code and JSON response from the GraphQL API.
