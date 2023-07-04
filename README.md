# Django E-commerce Backend



This repository contains the backend code for an e-commerce project built with Django. The backend provides APIs and handles the business logic and data management for the e-commerce application.

## Features

- User authentication and authorization
- Product management: Creating, updating, and deleting products
- Category management: Creating, updating, and deleting categories
- Order management: Processing orders, managing order status, and generating invoices
- Cart management: Adding products to the cart, updating quantities, and removing products from the cart

## Installation

1. Clone the project:
git clone https://github.com/zulaltasci/e-commerce-backend.git

2. Navigate to the project directory:
cd e-commerce-backend

3. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate # for Linux/Mac
venv\Scripts\activate.bat # for Windows

4. Install the dependencies:
pip install -r requirements.txt

5. Apply the database migrations:
python manage.py migrate


6. Run the development server:
python manage.py runserver

7. Open `http://localhost:8000` in your browser.

## API Documentation

The API documentation is available at `http://localhost:8000/swagger/` when the development server is running. It provides details about the available endpoints, request/response structures, and authentication requirements.

## Contributing

Pull requests for new features, bug fixes, or improvements are welcome. Please start a discussion by opening an issue before making any significant changes.

## License

This project is licensed under the [MIT License](LICENSE).
