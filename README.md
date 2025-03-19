# DoorService 🛠️

DoorService is a full-stack web application that connects customers with professional service providers for various household and maintenance needs. It offers seamless service request management, user registration, role-based dashboards, and real-time updates.
## 📌 Features

- 👤 **User Registration** with role selection (Customer / Professional)
- 📥 **Customer Dashboard** to create and manage service requests
- 🔧 **Professional Dashboard** to accept and update assigned tasks
- 🛠️ **Admin Panel** to manage users and search professionals/customers
- ✅ Role-based access control (CRUD for Admin, Read/Edit for Professionals, Limited Access for Customers)
## 🧱 Tech Stack

**Frontend**
- HTML5, CSS3, Bootstrap
- Vue.js

**Backend**
- Flask (Python)
- SQLAlchemy ORM
- Flask-Migrate

**Database**
- PostgreSQL (or SQLite for local development)

**Others**
- Redis + Celery (for async task handling)
- Gunicorn (for production WSGI server)
