"""
Dummy IRCTC API — mock endpoints for train status, PNR, and train name→number mapping.
Run with: uv run uvicorn main:app --reload
"""
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Dummy IRCTC API",
    description="Mock API for train status, PNR, and train mapping. Used by PRIMER and MCP samples.",
    version="0.1.0",
)

# Mock train number ↔ name mapping (resource-like)
TRAIN_MAPPING = [
    {"number": "12627", "name": "Karnataka Express"},
    {"number": "12682", "name": "Karnataka Express"},  # alternate
    {"number": "14682", "name": "Intercity Express"},
    {"number": "12345", "name": "Rajdhani Express"},
    {"number": "12245", "name": "Duronto Express"},
]

# Mock train running status (keyed by train number)
TRAIN_STATUS = {
    "12627": {
        "trainNo": "12627",
        "trainName": "Karnataka Express",
        "currentStation": "Bangalore City Junction (SBC)",
        "status": "Departed",
        "departureTime": "19:25",
        "scheduledDeparture": "19:20",
        "delayMinutes": 5,
        "remarks": "Running with minor delays (5 min at Hindupur, 10 min at Dharmavaram).",
    },
    "14682": {
        "trainNo": "14682",
        "trainName": "Intercity Express",
        "currentStation": "New Delhi (NDLS)",
        "status": "Arrived",
        "delayMinutes": 10,
        "remarks": "Train is at NEW DELHI, delayed by 10 mins.",
    },
    "12345": {
        "trainNo": "12345",
        "trainName": "Rajdhani Express",
        "currentStation": "Mumbai Central (MMCT)",
        "status": "On Time",
        "delayMinutes": 0,
    },
}

# Mock PNR status
def _mock_pnr(pnr: str) -> dict:
    return {
        "pnr": pnr,
        "trainNo": "12627",
        "trainName": "Karnataka Express",
        "from": "SBC",
        "to": "NDLS",
        "date": "2025-03-10",
        "bookingStatus": "CNF",
        "coach": "B2",
        "berth": "42",
        "passengers": [{"sr": 1, "berth": "42", "status": "CNF"}],
    }


@app.get("/")
def root():
    return {
        "name": "Dummy IRCTC API",
        "endpoints": {
            "train_status": "GET /train-status?train_no=12627",
            "pnr": "GET /pnr?pnr=YOUR_PNR",
            "train_mapping": "GET /train-mapping",
        },
    }


@app.get("/train-status")
def get_train_status(train_no: str = Query(..., description="Train number (e.g. 12627)")):
    """Mock train running status. Tool-like: invoke with train number."""
    train_no = train_no.strip()
    if train_no not in TRAIN_STATUS:
        return JSONResponse(
            status_code=404,
            content={"error": f"No mock status for train {train_no}", "train_no": train_no},
        )
    return TRAIN_STATUS[train_no]


@app.get("/pnr")
def get_pnr_status(pnr: str = Query(..., description="PNR number")):
    """Mock PNR status. Tool-like: invoke with PNR."""
    return _mock_pnr(pnr.strip())


@app.get("/train-mapping")
def get_train_mapping():
    """Mock train name → number mapping. Resource-like: read-only list."""
    return {"trains": TRAIN_MAPPING}


def run():
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
