# Career Portal (Flask + MySQL)

This is a full-stack job portal built using Flask, MySQL, and OOP principles in Python. It allows users to sign up, log in, view current job openings, and apply via a detailed form.

## Features

- User Signup/Login with hashed passwords
- Job Listings
- Job Application Forms
- OOP-based Flask App structure with SQLAlchemy

## How to Run

1. Clone the repository or unzip this project
2. Create a MySQL database named `jobportal`
3. Install requirements: `pip install flask flask_sqlalchemy werkzeug`
4. Run the app: `python run.py`
5. Visit `http://127.0.0.1:5000/`

## Database Setup

```sql
CREATE DATABASE jobportal;

-- You can populate Job table manually or add via Admin Panel later
```

## Folder Structure

```
career_portal/
│
├── run.py
├── README.md
└── app/
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── templates/
    │   ├── login.html
    │   ├── signup.html
    │   ├── jobs.html
    │   └── apply.html
    └── static/
```

---
Built with ❤️ using Flask and SQLAlchemy.
