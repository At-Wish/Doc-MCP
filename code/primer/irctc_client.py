"""
Client for the dummy IRCTC API. Used by the PRIMER loop as the "tools" backend.
Set IRCTC_API_BASE_URL (default http://127.0.0.1:8000) to point at code/irctc-api.
"""
import json
import os
import httpx

BASE_URL = os.environ.get("IRCTC_API_BASE_URL", "http://127.0.0.1:8000")


def get_train_status(train_no: str) -> str:
    """Live train running status. Calls GET /train-status?train_no=..."""
    train_no = (train_no or "").strip()
    if not train_no:
        return json.dumps({"error": "train_no is required"})
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as client:
        r = client.get("/train-status", params={"train_no": train_no})
        if r.status_code == 404:
            return json.dumps(r.json())
        r.raise_for_status()
        return json.dumps(r.json())


def get_pnr_status(pnr: str) -> str:
    """PNR ticket and seat status. Calls GET /pnr?pnr=..."""
    pnr = (pnr or "").strip()
    if not pnr:
        return json.dumps({"error": "pnr is required"})
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as client:
        r = client.get("/pnr", params={"pnr": pnr})
        r.raise_for_status()
        return json.dumps(r.json())


def get_train_number_mapping(_input: str = "") -> str:
    """Train name → number mapping (read-only). Calls GET /train-mapping."""
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as client:
        r = client.get("/train-mapping")
        r.raise_for_status()
        return json.dumps(r.json())
