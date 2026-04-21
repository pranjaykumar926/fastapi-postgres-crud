# FastAPI PostgreSQL CRUD API

A simple CRUD API built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.
This project demonstrates how to build a backend service with database integration using modern Python tools.

---

## 🚀 Features

* Create, Read, Update, Delete (CRUD) operations
* FastAPI framework for high performance APIs
* PostgreSQL database integration
* SQLAlchemy ORM
* Pydantic data validation
* Auto-generated API documentation (Swagger UI)

---

## 🛠 Tech Stack

* Python 3.10+
* FastAPI
* PostgreSQL
* SQLAlchemy
* Uvicorn
* Pydantic
* python-dotenv

---

## 📁 Project Structure

```
FASTAPI_POSTGRES/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── crud.py
│── requirements.txt
│── .env
│── .gitignore
│── venv/
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/pranjaykumar926/fastapi-postgres-crud.git
cd fastapi-postgres-crud
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:admin123@localhost:5432/bookstore
```

---

### 5. Run the server

```bash
uvicorn main:app --reload
```

---

## 📌 API Documentation

After running the server, open:

```
http://127.0.0.1:8000/docs
```

You will see interactive Swagger UI.

---

## 📊 Example Endpoints

### Create item

```
POST /items/
```

### Get all items

```
GET /items/
```

### Get item by ID

```
GET /items/{id}
```

### Update item

```
PUT /items/{id}
```

### Delete item

```
DELETE /items/{id}
```

---

## 🗄 Database

* Database name: `bookstore`
* Default user: `postgres`
* Port: `5432`

---

## 🔒 Notes

* Do NOT commit `.env` or `venv/` to GitHub
* Keep credentials secure

---

## 📈 Future Improvements

* JWT Authentication
* Pagination
* Docker support
* Alembic migrations
* Role-based access control

---

## 👨‍💻 Author

Pranjay Kumar
GitHub: [https://github.com/pranjaykumar926](https://github.com/pranjaykumar926)
