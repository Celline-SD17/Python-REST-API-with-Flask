from unittest.mock import patch
from openfoodfacts import fetch_product

@patch("openfoodfacts.requests.get")
def test_fetch(mock_get):
    mock_get.return_value.raise_for_status.return_value = None
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Nutella",
            "brand": "Ferrero",
            "ingredients_text": "Sugar, Palm oil, Hazelnuts"
        }
    }

    product = fetch_product("123456789012")
    assert product["product_name"] == "Nutella"
    assert product["brand"] == "Ferrero"