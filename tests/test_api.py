from app import app

client = app.test_client()
def test_get_inventory():
    response = client.get('/inventory')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert data[0]["product_name"] == "Nutella"
def test_add_item():
    response = client.post("/inventory", json={
        "barcode": "3017620422003",
        "price": 650,
        "stock": 10
    })
    assert response.status_code == 201