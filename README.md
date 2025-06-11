# Health Record API – Django + DRF

A secure, well-structured REST API to manage personal health records for patients and doctors, built using **Django** and **Django REST Framework**.

---

## 📌 Features

- JWT-based authentication with **5-minute token expiry**
- Patients can **create**, **view**, and **update** their own health records
- Doctors can only **view** and **comment** on records assigned to them
- **Strict access control** for secure health data
- **Signal-based notifications** when doctors are assigned to new patients
- **Celery-ready** for asynchronous background task support
- Clean, modular Django project structure with test coverage

---

## Tech Stack

- Python 3.12
- Django 4.x
- Django REST Framework
- SimpleJWT
- Celery (for background tasks)
- SQLite (default DB, easily swappable)

---

## Getting Started

### Installation
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

### Configuration
Ensure `settings.py` includes:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
}

AUTH_USER_MODEL = 'users.User'
```

### Migrate and Run
```bash
# Recreate all migrations
python manage.py makemigrations users
python manage.py makemigrations health_api
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## API Endpoints

### Auth
- `POST /api/users/register/` – Register (Patient/Doctor)
- `POST /api/token/` – Get JWT token
- `POST /api/token/refresh/` – Refresh access token

### Patient Actions
- `POST /api/records/` – Create new health record
- `GET /api/records/` – View own records

### Doctor Actions
- `GET /api/records/` – View assigned patient records
- `POST /api/comments/` – Comment on assigned records

---

## Background Notifications
- When a health record is created and assigned to a doctor, a Django signal triggers `notify_doctor_async`, which is Celery-ready for background execution.
- Optional: connect Redis and Celery to enable real async email sending.

---

## Running Tests
```bash
python manage.py test health_api
```
