# ENTREPIX – AI-Powered Customer Churn Prediction Web Application

ENTREPIX is an AI-powered web application designed to predict customer churn and provide actionable insights for customer retention. The system combines machine learning with a modern web interface to help businesses identify at-risk customers and take proactive measures.

This project was developed as part of the **ENTREPIX Entrepreneurship Event**, focusing on solving real-world business problems using data-driven intelligence.

---

## 🚀 Features

- 🔍 Predicts customer churn probability using machine learning
- 📊 Interactive dashboard with visual insights
- ⚡ Fast and lightweight API using FastAPI
- 🤖 Trained ML model integrated into a real-time web application
- 📈 Business-focused outputs for decision-making and retention strategies

---

## 🧠 Machine Learning Model

- **Model Type:** Supervised Classification  
- **Algorithms Used:** XGBoost / Scikit-learn  
- **Outputs:**
  - Churn Probability
  - Risk Category (Low / Medium / High)

The trained model is saved and loaded using `joblib` for efficient inference.

---

## 🏗️ Project Architecture

ENTREPIX-ML-Web-Application/
│
├── backend/
│ ├── main.py # FastAPI application
│ ├── model.pkl # Trained ML model
│ ├── requirements.txt # Backend dependencies
│
├── frontend/
│ ├── index.html # Dashboard UI
│ ├── style.css # Styling
│ ├── script.js # API integration & charts
│
├── README.md
└── .gitignore


---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Scikit-learn
- XGBoost
- Joblib
- Pydantic

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sachin-deepak-S/ENTREPIX-ML-Web-Application.git
cd ENTREPIX-ML-Web-Application
```
### 2️⃣ Backend Setup
```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
Backend runs at:
```
http://127.0.0.1:8000
```
### 3️⃣ Frontend Setup
Open frontend/index.html directly in a browser
(or use Live Server / any local web server)

## 🔗 API Usage
- Predict Churn
- Endpoint

### POST /predict
Sample Request
```
{
  "tenure": 12,
  "monthly_charges": 70.5,
  "total_charges": 850.3,
  "contract_type": 1
}
```
### Sample Response
```
{
  "churn_probability": 0.82,
  "risk_level": "High"
}
```
## 📊 Use Cases

- Customer retention strategy planning

- Business intelligence and analytics

- Startup churn analysis

- Academic and ML portfolio demonstration

## 🧪 Future Improvements

- User authentication (JWT)

- Model retraining pipeline

- Docker & deployment support

- CI/CD using GitHub Actions

- Model explainability (SHAP, feature importance)

## 🏅 Event Participation

Participated in ENTREPIX – Entrepreneurship Event

Presented an AI-powered customer churn prediction solution

Gained experience in innovation, teamwork, and business-focused ML applications

## 👥 Team Members

Sachin Deepak S

Sabarinath

Rohith P

Sabarish K

## 📄 License

This project is intended for educational and demonstration purposes.
