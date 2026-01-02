# Insurance Premium Category Prediction System

An end-to-end **Machine Learning project** that predicts the insurance premium
category for a user based on demographic and lifestyle information.

The system consists of:
- A **FastAPI backend** that serves an ML prediction API
- A **Streamlit frontend** that provides an interactive UI for users

---

## 🚀 Features
- ML-based insurance premium category prediction
- FastAPI backend with input validation using Pydantic
- Feature engineering using computed fields:
  - BMI
  - Age group
  - Lifestyle risk
  - City tier
- Streamlit frontend for easy user interaction
- Clean separation of backend and frontend

---

## 🛠 Tech Stack
- Python
- FastAPI
- Pydantic
- Scikit-learn
- Pandas
- Streamlit

---

## ⚙️ Project Structure
├── app.py # FastAPI backend (ML inference API)
├── frontend.py # Streamlit frontend
├── requirements.txt
├── model.pkl # Trained ML model (not tracked in Git)
└── README.md


---

## ▶️ How to Run Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
