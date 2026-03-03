from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

products = [
  { "id": 1, "name": "Tire A", "price": 100, "stock": 10 },
  { "id": 2, "name": "Tire B", "price": 150, "stock": 5 },
  { "id": 3, "name": "Tire C", "price": 200, "stock": 2 },
  { "id": 4, "name": "Tire D", "price": 250, "stock": 0 },
  { "id": 5, "name": "Tire E", "price": 300, "stock": 8 },
]

dealer_prices = {
    "PBT": {1: 2, 2: 140, 3: 190, 4: 240, 5: 290},
    "STG": {1: 90, 2: 135, 3: 180, 4: 230, 5: 280},
    "NFS": {1: 85, 2: 130, 3: 170, 4: 220, 5: 270},
}

@app.get("/")
def home():
    return {"message": "TirePro API"}

@app.get("/api/products")
def get_products():
    return {"data": products}

@app.get("/api/products/{dealer_code}")
def get_products_by_dealer(dealer_code: str):
    result = []
    for product in products:
        item = {
            "id": product["id"],
            "name": product["name"],
            "stock": product["stock"],
            "wholesale_price": product["price"],
        }
        if dealer_code in dealer_prices:
            item["contract_price"] = dealer_prices[dealer_code].get(product["id"], product["price"])
        else:
            item["contract_price"] = product["price"]
        result.append(item)
    return {"data": result}

