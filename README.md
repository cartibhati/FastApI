# Patient Management System API

A RESTful API built using **FastAPI** and **Pydantic** to manage patient records with
full CRUD functionality and computed health metrics.

---

## Features
- Create, view, update, and delete patient records
- Request and response validation using Pydantic
- Computed fields:
  - BMI
  - Health verdict
- Sort patients by height, weight, or BMI
- Auto-generated API documentation using Swagger (OpenAPI)

---

## Tech Stack
- Python
- FastAPI
- Pydantic
- JSON (file-based storage)

---

## How to Run Locally
```bash
pip install fastapi uvicorn
uvicorn main:app --reload
