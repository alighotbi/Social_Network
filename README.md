# 🧑‍🤝‍🧑 Social_Network

A simple yet functional social networking backend built with **Django** and **Django REST Framework**, where users can:

- Register and log in with **JWT Authentication**
- Create, delete, and view text-based posts
- Like and comment on posts
- Add and manage friendships

> **Note:** This project currently has no frontend — it's fully API-based with a Swagger UI for easy testing.

---

## 📌 Features

- ✅ User Registration & Login (JWT)
- ✅ Post Creation & Deletion
- ✅ Like & Comment System
- ✅ Friendships (Add / Remove Friends)
- ✅ RESTful API with Swagger Documentation

---

## 🧱 Tech Stack

| Layer        | Technology               |
|--------------|--------------------------|
| Backend      | Django, Django REST Framework |
| Auth         | JWT (via `djangorestframework-simplejwt`) |
| Database     | MySQL                    |
| Docs / UI    | Swagger (via `drf-spectacular`) |
| Dev Tools    | pip, virtualenv          |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/alighotbi/Social_Network.git
cd Social_Network
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Install dependencies
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
### 5. Run migrations
```python
python manage.py makemigrations
python manage.py migrate
```
### 6. Create a superuser (optional)
```bash
python manage.py createsuperuser
```
### 7. Run the server
```bash
python manage.py runserver
```
----
