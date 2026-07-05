# Inventory Management System
## Overview
- The Inventory Management System is a Flask-based REST API that allows employees to manage inventory through a Command Line Interface(CLI).
- The application performs CRUD (Create, Read, Update, Delete) operations on inventory items while integrating with the OpenFoodFacts API to retrieve product information using a barcode.
- A python list is used to simulate temporary data storage, facilitating the implementation of Flask operations such as REST APIs, external API integration, and Flask development. 
## Features
   * View all inventory items.
   * View a single inventory item by ID.
   * Add new inventory items.
   * Update item prices and stock levels.
   * Delete inventory items.
   * Search products using the OpenFoodFacts API.
   * Automatically retrieve product details from OpenFoodFacts when adding new products.
   * CLI interface for interacting with the API.
   * Unit tests using pytest and unittest.mock.
## Technologies Used
1. Python3
2. Flask
3. Requests
4. Pytest
5. Unittest.mock
6. OpenFoodFacts API
## Project Structure

```
Inventory-Management-System/ 
│ 
├── app.py              # Flask REST API 
├── cli.py              # Command Line Interface 
├── inventory.py        # Temporary inventory storage 
├── openfoodfacts.py    # External API integration 
├── requirements.txt 
├── pytest.ini 
│ 
└── tests/ 
    ├── test_api.py 
    ├── test_cli.py 
    └── test_openfoodfacts.py
```
## Installation
1. Clone my github respository
    - git clone ([[https://github.com/Celline-SD17/Python-REST-API-with-Flask]])
2. Create a virtual environment:
    - For Linux/macOs, run command: python3 -m venv venv
    - For Windows , run command:  python -m venv venv
3. Activate the virtual ebvironment:
    - For Linux/macOS, run command: source/venv/bin/activate
    - For Windows, run command: venv\Scripts\activate
4. Install the required packages
    - pip install -r requirements.txt

## Running the Application
- Step 1: Start the Flask server: 
    * Run the command: python3 app.py
    -The API will run on "http://127.0.0.1:5000"
- Step 2: Open another terminal with the virtual environment activated:
    * Run the command: pythom3 cli.py
    ### CLI Menu
    - When the CLI app starts, it displays the following menu:
        1. View Inventory 
        2. View Item by ID 
        3. Add Item 
        4. Update Item 
        5. Delete Item 
        6. Search Product by Barcode 
         7. Exit
    #### Menu Options:
    1. View Inventory
        - Displays all products currently stored in the inventory.
    2. View Item by ID
        - Retrieves a specific inventory item using its unique ID.
    3. Add Item
        - Enter a product barcode.
        - The application searches OpenFoodFacts.
        - Product details are displayed.
        - Enter the selling price and stock quantity.
        - The product is added to the inventory.
    4. Update Item
    - Allows updating:
        - Product price
        - Product stock
    - using the inventory ID.
    5. Delete Item
    - Removes a product from the inventory using its ID.
    6. Search Product by Barcode
    - Searches the OpenFoodFacts database using a barcode and displays the product information without adding it to the inventory.
    7. Exit
    - Closes the CLI application.
```
REST API Endpoints


Method	   Endpoint	             Description

GET	       /inventory	          Retrieve all inventory items
GET	       /inventory              Retrieve a single inventory item
POST	   /inventory	          Add a new inventory item
PATCH	   /inventory/<id>	      Update price or stock
DELETE	   /inventory/<id>	      Delete an inventory item
GET	       /product/<barcode>	  Search OpenFoodFacts by barcode
```

## OpenFoodFacts Integration
- The application integrates with the OpenFoodFacts API to retrieve product information using a barcode.
- Information retrieved includes:
    * Barcode
    * Product name
    * Brand
    * Ingredients
- The retrieved information is combined with employee- entered data (price and stock) before being stored in the inventory list. 
## Temporary Data Storage
- This project uses a Python list located in inventory.py to simulate a database.
- Because the data is stored in memory:
    - New products are available while the application is running.
    - Restarting the Flask server resets the inventory to its original contents. 
## Running Tests
- Run all tests with:
  -pytest
- The test suite covers:
  * Flask API endpoints
  * CLI functionality
  * OpenFoodFacts integration using mocked API responses
## Error Handling
- The application handles:
    * Invalid inventory IDs
    * Missing products
    * Invalid barcodes
    * Failed external API requests
    * Invalid menu selections
## Future Improvements
- Potential enhancements include:
    * Replace the temporary list with a real database (SQLite or PostgreSQL)
    * Add user authentication
    * Improve CLI formatting
    * Prevent duplicate inventory items
    * Add inventory reports and analytics
## Author
- Developed as a Flask REST API and CLI inventory management school project demonstrating CRUD operations, external API integration, testing, and RESTful application design.















