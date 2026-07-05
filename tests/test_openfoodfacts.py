from unittest.mock import patch
from openfoodfacts import fetch_product

@patch("openfoodfacts.requests.get")
def test_fetch(mock_get):
    mock_get.return_value.json.return_value = {
        "product": {
            "product_name": "Nutella",
            "brand": "Ferrero",
            "ingredients": "Sugar, Palm oil, Hazelnuts"
        }
    }

    product = fetch_product("123456789012")
    assert product["product_name"] == "Nutella"