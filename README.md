# CRUD Flask ✅

This project is a simple CRUD (Create, Read, Update, Delete) application built using Flask, a Python web framework. It demonstrates basic operations with a MySQL database, allowing management of customers, products, orders, and order items.

## Features

- **Customer Management:** Add, view, edit, and delete customers.
- **Product Management:** Add, view, edit, and delete products.
- **Order Management:** Create and manage orders, including adding and removing order items.
- **Order Item Management:** Add items to orders and remove them as needed.

## Project Structure

```plaintext
CRUD_Flask/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
│       ├── index.html
│       ├── add_customer.html
│       ├── list_customers.html
│       ├── edit_customer.html
│       ├── add_product.html
│       ├── list_products.html
│       ├── edit_product.html
│       ├── list_orders.html
│       ├── add_order.html
│       ├── edit_order.html
│       ├── add_order_item.html
│       └── edit_order_item.html
```

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/CRUD_Flask.git
   cd CRUD_Flask

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Configure the database:**
- Ensure you have MySQL installed and running.
- Create a MySQL database named store_db.
- Update the database configuration in app/__init__.py with your MySQL credentials.
4. **Initialize the database:**
    ```bash
    flask db init
    flask db migrate
    flask db upgrade

5. **Run the application:**
    ```bash
    flask run
6. **Access the application:**

Open your web browser and navigate to http://127.0.0.1:5000/.

## Usage

- Add a new customer: Navigate to /customers/add.
- View the product list: Navigate to /products.
- Add an order: Navigate to /orders/add.
- And so on, using the URLs and functionalities described.

## Contribution

If you would like to contribute to the project, feel free to open issues or pull requests. Any help is welcome! 🤝