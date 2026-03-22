"""
Client for the dummy IRCTC API. Used by the MCP server to implement tools and resources.
"""
import json
import os
import httpx

BASE_URL = os.environ.get("IRCTC_API_BASE_URL", "http://127.0.0.1:8000")


def get_train_status(train_no: str) -> dict:
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as client:
        r = client.get("/train-status", params={"train_no": train_no.strip()})
        if r.status_code == 404:
            return r.json()
        r.raise_for_status()
        return r.json()


def get_pnr_status(pnr: str) -> dict:
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as client:
        r = client.get("/pnr", params={"pnr": pnr.strip()})
        r.raise_for_status()
        return r.json()


def get_train_mapping() -> dict:
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as client:
        r = client.get("/train-mapping")
        r.raise_for_status()
        return r.json()
