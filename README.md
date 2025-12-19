# 🍽️ Django Restaurant Reservation System

A modern, elegant web application for restaurant table reservations built with Django 5.2, featuring a beautiful responsive UI, user authentication, and complete reservation management.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🎨 Modern & Responsive Design
- Beautiful gradient UI with smooth animations
- Fully responsive design (mobile, tablet, desktop)
- Modern card-based layout for restaurants
- Professional color scheme and typography

### 👤 User Management
- User registration and authentication
- Login/logout functionality
- Personalized user dashboard
- User profile integration

### 🍴 Restaurant Features
- Restaurant listing with detailed information
- Restaurant cards with images, ratings, and descriptions
- Cuisine type categorization
- Opening hours display
- Phone and address information
- Real-time table availability

### 📅 Reservation System
- Interactive reservation form
- Date and time selection with validation
- Guest count selection
- Special requests field
- Reservation status tracking (Pending, Confirmed, Cancelled, Completed)
- View all user reservations in dashboard
- Cancel reservations

### 🔐 Security
- Login-required views for sensitive operations
- CSRF protection
- User-specific reservation access
- Secure password handling

### 🛠️ Admin Panel
- Enhanced Django admin interface
- Restaurant management
- Table management with availability toggle
- Reservation management with status updates
- Search and filter capabilities

### 🌐 REST API
- API endpoints for restaurants, tables, and reservations
- Django REST Framework integration
- JSON responses for external integrations

## 📋 Requirements

- Python 3.9+
- Django 5.2+
- Django REST Framework
- SQLite (default) or PostgreSQL

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Django-Restaurant
```

### 2. Create and activate virtual environment

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install django djangorestframework
# or if requirements.txt exists:
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### 6. Populate sample data (optional but recommended)
```bash
python populate_data.py
```
This will create 5 sample restaurants with tables.

### 7. Run the development server
```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## 📱 Usage

### Public Pages
- **Home Page**: `http://127.0.0.1:8000/`
  - Browse all available restaurants
  - View restaurant details, ratings, and available tables
  - Beautiful card-based layout with images

### User Authentication
- **Register**: `http://127.0.0.1:8000/register/`
  - Create a new user account
  - Automatic login after registration

- **Login**: `http://127.0.0.1:8000/login/`
  - Access your account
  - Required for making reservations

### Reservations (Login Required)
- **Make Reservation**: `http://127.0.0.1:8000/reserve/`
  - Select table, date, time
  - Specify number of guests
  - Add special requests

- **My Dashboard**: `http://127.0.0.1:8000/dashboard/`
  - View all your reservations
  - Check reservation status
  - Cancel reservations

- **Success Page**: `http://127.0.0.1:8000/success/`
  - Confirmation after successful reservation

### Admin Panel
- **Admin**: `http://127.0.0.1:8000/admin/`
  - Manage restaurants, tables, and reservations
  - Update reservation status
  - Toggle table availability

### REST API Endpoints
- **Restaurants**: `http://127.0.0.1:8000/api/restaurants/`
- **Tables**: `http://127.0.0.1:8000/api/tables/`
- **Reservations**: `http://127.0.0.1:8000/api/reservations/`

## 🏗️ Project Structure

```
Django-Restaurant/
├── django_restaurant/          # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
│
├── restaurant/                 # Main application
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files
│   │   └── restaurant/
│   │       ├── css/
│   │       │   └── style.css  # Main stylesheet
│   │       ├── js/            # JavaScript files
│   │       └── images/        # Image assets
│   │
│   ├── templates/             # HTML templates
│   │   └── restaurant/
│   │       ├── base.html      # Base template
│   │       ├── restaurant_list.html
│   │       ├── make_reservation.html
│   │       ├── reservation_success.html
│   │       ├── dashboard.html
│   │       ├── login.html
│   │       └── register.html
│   │
│   ├── models.py              # Data models
│   ├── views.py               # View functions
│   ├── forms.py               # Form definitions
│   ├── urls.py                # App URL patterns
│   ├── admin.py               # Admin configuration
│   ├── serializers.py         # DRF serializers
│   └── api_views.py           # API views
│
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django management script
├── populate_data.py            # Sample data script
└── README.md                   # This file
```

## 🗄️ Database Models

### Restaurant
- `name`: Restaurant name
- `address`: Physical address
- `phone`: Contact phone number
- `description`: Restaurant description
- `image`: Restaurant image URL
- `cuisine_type`: Type of cuisine
- `opening_time`: Opening time
- `closing_time`: Closing time
- `rating`: Restaurant rating (0-5)
- `created_at`: Creation timestamp

### Table
- `restaurant`: Foreign key to Restaurant
- `number`: Table number
- `capacity`: Number of seats
- `is_available`: Availability status

### Reservation
- `user`: Foreign key to User
- `table`: Foreign key to Table
- `date`: Reservation date
- `time`: Reservation time
- `status`: Status (pending, confirmed, cancelled, completed)
- `guests`: Number of guests
- `special_requests`: Special requests text
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

## 🎨 Key Features Explained

### Modern UI/UX
- **Gradient backgrounds** for visual appeal
- **Card-based layouts** for easy scanning
- **Hover effects** for interactivity
- **Responsive grid system** adapts to all screen sizes
- **Professional color scheme** with primary and secondary colors
- **Smooth animations** for better user experience

### Smart Form Design
- **Date validation** (no past dates)
- **Form field styling** with focus effects
- **Error handling** with clear messages
- **Success feedback** after actions
- **Placeholder text** for guidance

### Security Features
- **LoginRequiredMixin** for protected views
- **CSRF protection** on all forms
- **User-specific data access**
- **Password validation**
- **Secure session management**

## 🔧 Configuration

### Static Files
Static files are configured in `settings.py`:
```python
STATIC_URL = "static/"
```

### Database
Default configuration uses SQLite. To switch to PostgreSQL, update `DATABASES` in `settings.py`.

### Authentication
Login redirect URL can be configured in views or settings:
```python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'restaurant_list'
```

## 🚀 Deployment Tips

1. **Set DEBUG to False** in production
2. **Configure ALLOWED_HOSTS** with your domain
3. **Use environment variables** for SECRET_KEY
4. **Set up static file serving** (WhiteNoise or CDN)
5. **Use PostgreSQL** instead of SQLite
6. **Configure email backend** for notifications
7. **Set up HTTPS** with SSL certificate

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👥 Author

Created with ❤️ by Yussef

## 🙏 Acknowledgments

- Django Framework
- Django REST Framework
- Unsplash for sample images
- Modern CSS design patterns

## 📞 Support

For support, please open an issue in the GitHub repository.

---

**Enjoy your restaurant reservation system! 🍽️✨**
