# Bulk Product Management API

This is a simple Bulk Product Management API built with Django and Django REST Framework (DRF). It allows for managing products and their variants. Users can perform operations like creating, updating, deleting, and retrieving products and their variants. The API also includes a user interface where users can upload product images and view product details along with their variants.

## Features
- **Products**: Create, list, retrieve, update, and delete products.
- **Product Variants**: Create, list, retrieve, update, and delete product variants.
- **Image Upload**: Upload product images.
- **User Interface**: View uploaded products and their variants from the user interface.
- **DRF Interface**: Products and variants can also be managed through the DRF interface.

## Models

### Product Model
The Product model includes:
- `id`: Unique identifier for the product.
- `name`: Name of the product.
- `image`: Product image, which is optional.

### ProductVariant Model
The ProductVariant model includes:
- `id`: Unique identifier for the product variant.
- `sku`: Stock Keeping Unit (unique identifier for the variant).
- `name`: Name of the product variant.
- `price`: Price of the product variant.
- `details`: Additional details about the product variant.
- `product`: ForeignKey referencing the `Product` model.

## API Endpoints

### Products
- **List and Create Products**
  - **Endpoint**: `GET /products/` (List products) and `POST /products/` (Create new product)
- **Retrieve, Update, and Delete Product**
  - **Endpoint**: `GET /api/products/<int:pk>/` (Retrieve a product)
  - **PUT /api/products/<int:pk>/` (Update a product)
  - **DELETE /api/products/<int:pk>/` (Delete a product)

### Product Variants
- **List and Create Product Variants**
  - **Endpoint**: `GET /variants/` (List product variants) and `POST /variants/` (Create new product variant)
- **Retrieve, Update, and Delete Product Variant**
  - **Endpoint**: `GET /api/variants/<int:pk>/` (Retrieve a product variant)
  - **PUT /api/variants/<int:pk>/` (Update a product variant)
  - **DELETE /api/variants/<int:pk>/` (Delete a product variant)

## Generics
In this project, **generics** are used to create the views for products and product variants. The use of generics provides more flexibility, allowing for the automatic generation of common views such as listing, creating, retrieving, updating, and deleting products and variants.

**ViewSets** can also be used for more complex use cases, but in this case, generics are preferred for their simplicity and flexibility.

## User Interface
Once the server is running, you can view the user interface at `http://localhost:8000/`. This page displays a list of products and their variants, and you can also upload product images through the UI. Alternatively, you can manage products and variants via the DRF API interface at `http://localhost:8000/api/products`.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jerrynabango/Bulk-API
   ```

2. **Install Dependencies**:
   Ensure you have `pip` installed. Then, install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, if you don't have a `requirements.txt` file, install each dependency manually:
   ```bash
   pip install django
   pip install djangorestframework
   ```

3. **Migrate the Database**:
   Run the following command to apply the initial migrations:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

4. **Run the Development Server**:
   Start the Django development server:
   ```bash
   python3 manage.py runserver
   ```

5. **Access the Application**:
   - **API**: You can interact with the API at `http://localhost:8000/api/products/` and `http://localhost:8000/api/variants/`.
   - **User Interface**: View the products and variants at `http://localhost:8000/`.

6. **Running Tests**:
   To ensure everything is working correctly, you can run the tests using:
   ```bash
   python3 manage.py test
   ```

## Usage
- You can interact with the API through both the Django user interface and DRF interface.
- Products can be posted, edited, and deleted using the API.
- Variants of products can also be managed through the API.

## Contributing
Feel free to fork the repository and submit a pull request for any improvements or fixes.

## License
This project is licensed under the MIT License.
