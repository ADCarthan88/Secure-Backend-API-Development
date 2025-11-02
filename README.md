# Secure Backend API Development

A secure, scalable REST API built with Django REST Framework featuring JWT authentication, input validation, and comprehensive security measures.

## Features

- **JWT Authentication** - Secure token-based authentication with refresh tokens
- **Input Validation** - Strong password requirements and email validation
- **Rate Limiting** - Protection against brute force attacks
- **CORS Protection** - Configured for specific origins
- **Security Headers** - XSS protection, content type validation
- **User Management** - Registration, login, profile management
- **Post Management** - CRUD operations for user posts

## API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `POST /api/auth/change-password/` - Change password
- `GET /api/auth/profile/` - Get user profile
- `POST /api/auth/token/refresh/` - Refresh JWT token

### Users
- `GET/PUT /api/users/profile/` - User profile management
- `GET /api/users/posts/` - List all posts
- `POST /api/users/posts/` - Create new post
- `GET/PUT/DELETE /api/users/posts/<id>/` - Manage specific post
- `GET /api/users/my-posts/` - Get user's posts

## Quick Start

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Create superuser (optional):**
```bash
python manage.py createsuperuser
```

4. **Start development server:**
```bash
python manage.py runserver
```

5. **Test the API:**
```bash
python test_api.py
```

## Security Features

- JWT token authentication with blacklisting
- Strong password validation (8+ chars, uppercase, lowercase, digit, special char)
- Rate limiting on authentication endpoints
- CORS protection
- XSS and CSRF protection
- SQL injection prevention via Django ORM
- Secure password hashing

## Environment Variables

Create a `.env` file with:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

## Example Usage

### Register a new user:
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "SecurePass123!",
    "password_confirm": "SecurePass123!"
  }'
```

### Login:
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePass123!"
  }'
```

### Access protected endpoint:
```bash
curl -X GET http://localhost:8000/api/auth/profile/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Production Deployment

1. Set `DEBUG=False` in settings
2. Configure proper database (PostgreSQL recommended)
3. Set strong `SECRET_KEY`
4. Configure HTTPS
5. Set up proper CORS origins
6. Use environment variables for sensitive data

## License

MIT License