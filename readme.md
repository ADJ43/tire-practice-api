# TirePro Practice API

FastAPI backend for the TirePro practice eCommerce application.

## Tech Stack
- Python 3 / FastAPI
- Uvicorn (ASGI server)

## Endpoints
- `GET /api/products` — Returns all products with wholesale pricing
- `GET /api/products/{dealer_code}` — Returns products with dealer-specific contract pricing (PBT, STG, NFS)
- `GET /docs` — Swagger UI documentation

## Setup
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
uvicorn main:app --reload
```

## Frontend
Pair with [tire-practice](https://github.com/ADJ43/tire-practice) React app running on port 3000.