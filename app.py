from flask import Flask, jsonify, request
from inventory import inventory
from openfoodfacts import fetch_product

app = Flask(__name__)

#Home
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Inventory Management System"}), 200

#Fetching all items
@app.route('/inventory', methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200

#Fetching a single item by ID
@app.route('/inventory/<int:id>', methods=["GET"])
def get_item(id):
    item = next((item for item in inventory if item["id"] == id), None)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not Found"}), 404

#Adding an Item
@app.route('/inventory', methods=["POST"])
def add_item():
    data = request.get_json()
    barcode = data.get("barcode")
    price = data.get("price")
    stock = data.get("stock")

    if not barcode:
        return jsonify({"error": "Barcode is required"}), 400
    if price is None:
        return jsonify({"error": "Price is required"}), 400
    if stock is None:
        return jsonify({"error": "Stock is required"}), 400
    
    api_product = fetch_product(barcode)
    if api_product is None:
        return jsonify({"error": "Item not found"}), 404
    new_item = {
        "id" : max(item["id"] for item in inventory) + 1 if inventory else 1,
        "barcode": barcode,
        "product_name": api_product['product_name'],
        "brand": api_product["brand"],
        "ingredients": api_product["ingredients"],
        "price": price,
        "stock": stock
    }
    inventory.append(new_item)
    return jsonify(new_item), 201
#Updating stock levels or Item prices
@app.route('/inventory/<int:id>', methods=["PATCH"])
def update_item(id):
    item = next((item for item in inventory if item["id"] == id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    
    data = request.get_json()
    price = data.get("price")
    stock = data.get("stock")

    if price is not None:
        item["price"] = price
    if stock is not None:
        item["stock"] = stock
    return jsonify(item), 200

#Deleting an item
@app.route('/inventory/<int:id>', methods=["DELETE"])
def delete_item(id):
    item = next((item for item in inventory if item["id"] == id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    
    inventory.remove(item)
    return jsonify({"message": "Item deleted successfully"}), 200

#Searching an Item by barcode
@app.route('/product/<barcode>', methods=["GET"])
def search_API(barcode):
    product = fetch_product(barcode)
    if product is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(product), 200

if __name__ == '__main__':
    app.run(debug=True)
    