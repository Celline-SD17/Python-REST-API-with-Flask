import requests
BASE_URL = "http://127.0.0.1:5000"

#Viewing Inventory
def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    print(response.json())

#View One Item
def view_item():
    item_id = input("Enter the item ID: ")
    response = requests.get(f"{BASE_URL}/inventory/{item_id}")
    print(response.json())

#Add Items
def add_item():
    barcode = input("Enter the item barcode: ")
    response = requests.get(f"{BASE_URL}/product/{barcode}")
    if response.status_code != 200:
        print("Product not found in OpenFoodFacts API.")
        return
    product= response.json()
    print("\nProduct found.")
    print(f"Name: {product['product_name']}")
    print(f"Brand: {product['brand']}")
    print(f"ingredients: {product['ingredients']}")

    choice = input("\nAdd this product to inventory? (y/n): ").lower()
    if choice != "y":
        print("Product not added.")
        return
    price = float(input("Enter the selling price: "))
    stock = int(input("Enter the stock quantity: "))
    data = {
        "barcode": barcode,
        "price": price,
        "stock": stock
    }
    response = requests.post(f"{BASE_URL}/inventory", json=data)
    print(response.json())

#Update Item
def update_item():
    item_id = input("Enter the item ID: ")
    data = {}
    price = input("Enter the new price: ")
    stock = input("Enter the new stock: ")

    if price:
        data["price"] = float(price)
    if stock:
        data["stock"] = int(stock)
    response = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=data)
    print(response.json())

# Delete Item
def delete_item():
    item_id = input("Enter the item ID:")
    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")
    print(response.json())

#Searching Item by barcode from OpenFoodFacts API
def search_product():
    barcode = input("Enter product barcode: ")
    response = requests.get(f"{BASE_URL}/product/{barcode}")
    print(response.json())


def menu():
    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. View Item by id")
        print("3. Add Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Search Product by Barcode")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            view_item()
        elif choice == "3":
            add_item()
        elif choice == "4":
           update_item()
        elif choice == "5":
           delete_item()
        elif choice == "6":
            search_product()
        elif choice == "7":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
