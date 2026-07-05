import requests
BASE_URL = "https://world.openfoodfacts.net/api/v2/product"

def fetch_product(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if data.get("status") != 1:
            return None
        product = data["product"]

        return {
            "barcode": barcode,
            "product_name": product.get("product_name", "unknown"),
            "brand": product.get("brand", "Unknown"),
            "ingredients": product.get("ingredients_text", "Not Available")
        }
    except requests.exceptions.RequestException:
        return None 
