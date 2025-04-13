# 🛒 PhiMart - eCommerce API

PhiMart is a full-featured eCommerce backend project built with Django REST Framework (DRF). It provides essential API endpoints for managing products, categories, cart, and orders. It also features secure user authentication using JWT via Djoser and includes auto-generated Swagger documentation using drf_yasg.

---

## 🚀 Features

- ✅ Product Management API
- ✅ Category Management API
- ✅ Cart Functionality
- ✅ Order Processing System
- ✅ JWT Authentication with Djoser
- ✅ Swagger Documentation with drf_yasg

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (via Djoser)
- **Documentation**: Swagger UI (drf_yasg)
- **Database**: SQLite / PostgreSQL (configurable)

---

## 📚 API Documentation

Once the server is running, access the interactive Swagger docs at:  
📍 `http://localhost:8000/swagger/`




---

## 🔐 Authentication

- JWT-based authentication with Djoser
- Includes endpoints for user registration, login, token refresh, etc.

Example endpoints:

| Method | Endpoint              | Description               |
|--------|-----------------------|---------------------------|
| POST   | `/auth/users/`        | Register a new user       |
| POST   | `/auth/jwt/create/`   | Obtain access/refresh token |
| POST   | `/auth/jwt/refresh/`  | Refresh access token      |

---

## 🧪 Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/phimart.git
cd phimart

### 2. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


### 3. Install Requirements

pip install -r requirements.txt


### 4. Run Migrations

python manage.py migrate


### 5. Start Development Server

python manage.py runserver



---

Let me know if you’d like help generating the `requirements.txt` or adding example `.env` configs.

# PhiMart
