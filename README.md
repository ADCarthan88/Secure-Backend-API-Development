# 🔐 Secure Backend API Development

<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white" alt="Django REST Framework">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white" alt="JWT">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</div>

<div align="center">
  <h3>🚀 Enterprise-grade REST API with bulletproof security</h3>
  <p>A production-ready backend API featuring JWT authentication, comprehensive input validation, and advanced security measures built with Django REST Framework.</p>
</div>

---

## 🎯 What This App Does

This secure backend API provides a robust foundation for modern web applications, offering:

- **🔐 Secure User Authentication** - JWT-based auth system with refresh tokens
- **👤 User Management** - Complete user registration, login, and profile management
- **📝 Content Management** - CRUD operations for user-generated content (posts)
- **🛡️ Enterprise Security** - Multiple layers of protection against common vulnerabilities
- **⚡ High Performance** - Optimized for scalability and speed
- **📊 API Documentation** - Well-documented endpoints for easy integration

## ✨ Key Features

### 🔒 **Security First**
- **JWT Authentication** with access & refresh tokens
- **Strong Password Policy** (8+ chars, mixed case, numbers, symbols)
- **Rate Limiting** to prevent brute force attacks
- **CORS Protection** with configurable origins
- **XSS & CSRF Protection** via security headers
- **SQL Injection Prevention** through Django ORM
- **Secure Password Hashing** with Django's built-in system

### 🚀 **Developer Experience**
- **RESTful API Design** following industry standards
- **Comprehensive Input Validation** with detailed error messages
- **Automated Testing** with included test suite
- **Environment Configuration** for different deployment stages
- **Clean Code Architecture** with separation of concerns
- **Detailed Documentation** with usage examples

### 📱 **User Features**
- User registration with email validation
- Secure login/logout functionality
- Profile management and updates
- Password change with validation
- Personal content creation and management
- Token refresh for seamless sessions

## 🛠️ Tech Stack

### **Backend Framework**
- **Django 4.2.7** - High-level Python web framework
- **Django REST Framework 3.14.0** - Powerful toolkit for building APIs
- **Django CORS Headers** - Cross-Origin Resource Sharing support

### **Authentication & Security**
- **djangorestframework-simplejwt 5.3.0** - JWT authentication
- **python-decouple 3.8** - Environment variable management
- **cryptography 41.0.7** - Cryptographic recipes and primitives

### **Database**
- **SQLite** (Development) - Lightweight database
- **PostgreSQL** (Production Ready) - Enterprise database support

### **Additional Tools**
- **Rate Limiting** - Built-in throttling mechanisms
- **Input Validation** - Custom validators for data integrity
- **Security Headers** - XSS, CSRF, and content type protection

## 📸 API Screenshots

### 🔐 Authentication Flow
```json
// POST /api/auth/register/
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "password_confirm": "SecurePass123!"
}

// Response
{
  "message": "User registered successfully",
  "user_id": 1,
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 👤 User Profile Management
```json
// GET /api/auth/profile/
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "date_joined": "2024-01-15T10:30:00Z",
  "is_active": true
}
```

### 📝 Content Creation
```json
// POST /api/users/posts/
{
  "title": "My First Secure Post",
  "content": "This post was created using the secure API!"
}

// Response
{
  "id": 1,
  "title": "My First Secure Post",
  "content": "This post was created using the secure API!",
  "author": "johndoe",
  "created_at": "2024-01-15T10:35:00Z",
  "is_published": true
}
```

## 🌐 Live Demo

### 🚀 **Quick Test Drive**

1. **Clone and Run Locally:**
```bash
git clone https://github.com/ADCarthan88/Secure-Backend-API-Development.git
cd Secure-Backend-API-Development
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

2. **Test the API:**
```bash
python test_api.py
```

3. **Interactive API Testing:**
   - Visit `http://localhost:8000/admin/` for Django admin
   - Use tools like Postman or curl to test endpoints
   - Check the `test_api.py` file for example requests

### 📋 **API Endpoints Overview**

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register/` | User registration | ❌ |
| POST | `/api/auth/login/` | User login | ❌ |
| POST | `/api/auth/logout/` | User logout | ✅ |
| GET | `/api/auth/profile/` | Get user profile | ✅ |
| POST | `/api/auth/change-password/` | Change password | ✅ |
| POST | `/api/auth/token/refresh/` | Refresh JWT token | ❌ |
| GET/PUT | `/api/users/profile/` | Manage user profile | ✅ |
| GET/POST | `/api/users/posts/` | List/Create posts | ✅ |
| GET/PUT/DELETE | `/api/users/posts/<id>/` | Manage specific post | ✅ |
| GET | `/api/users/my-posts/` | Get user's posts | ✅ |

## 🚀 Quick Start Guide

### 1️⃣ **Installation**
```bash
# Clone the repository
git clone https://github.com/ADCarthan88/Secure-Backend-API-Development.git
cd Secure-Backend-API-Development

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ **Database Setup**
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 3️⃣ **Start Development Server**
```bash
python manage.py runserver
```

### 4️⃣ **Test the API**
```bash
# Run automated tests
python test_api.py

# Or test manually with curl
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "SecurePass123!",
    "password_confirm": "SecurePass123!"
  }'
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=secure_api_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### Production Deployment Checklist
- [ ] Set `DEBUG=False`
- [ ] Configure PostgreSQL database
- [ ] Set strong `SECRET_KEY`
- [ ] Configure HTTPS
- [ ] Update `ALLOWED_HOSTS`
- [ ] Set proper CORS origins
- [ ] Configure static files serving
- [ ] Set up monitoring and logging

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <p>Built with ❤️ using Django REST Framework</p>
  <p>⭐ Star this repo if you found it helpful!</p>
</div>