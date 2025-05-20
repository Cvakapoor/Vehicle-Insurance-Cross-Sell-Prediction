# Vehicle Insurance Cross-Sell Prediction 🚗📊

This project aims to predict whether a customer is interested in purchasing vehicle insurance, based on demographic, vehicle, and policy-related data. It leverages Apache Spark for scalable ETL, XGBoost for high-performance modeling, and FastAPI for deployment. MLflow is used for experiment tracking, and Docker + Kubernetes are used for containerization and orchestration.

---

## 🚀 Features

- **ETL with Apache Spark**: Efficient data loading, cleaning, and transformation at scale.
- **Modeling with XGBoost**: Gradient boosting classifier for binary prediction.
- **API with FastAPI**: Serve predictions via a RESTful endpoint.
- **MLflow Integration**: Log metrics and track experiments.
- **Docker & Kubernetes**: Seamless deployment and scalability.

---

## 🧪 Setup Instructions

### 1. Clone the Repository

<pre>git clone https://github.com/yourusername/vehicle_insurance_prediction.git</pre>
<pre>cd vehicle_insurance_prediction</pre>

### 2. Install Dependencies

Create a virtual environment and install requirements:

<pre>python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt</pre>

---

## ⚙️ Run the Pipeline

### 1. Run Spark ETL

<pre>python etl/spark_etl.py</pre>

This saves a cleaned CSV in the data/processed_train.csv.

### 2. Train the Model

<pre>python model/train.py</pre>

The best model is saved as model/xgb_model.json, and logs are stored in the mlruns/ directory.

### 3. Make Predictions

<pre>python model/predict.py</pre>

This generates predictions on the test set and saves them as predictions.csv.

---

## 🌐 API Usage

### Start the FastAPI Server

<pre>uvicorn api.app:app --reload</pre>

### Example Request

POST /predict
{
  "Gender": "Male",
  "Age": 35,
  "Driving_License": 1,
  "Region_Code": 28,
  "Previously_Insured": 0,
  "Vehicle_Age": "1-2 Year",
  "Vehicle_Damage": "Yes",
  "Annual_Premium": 35000,
  "Policy_Sales_Channel": 26,
  "Vintage": 200
}

### Example Response

{
  "prediction": 1
}

---

## 🐳 Docker Deployment

### Build the Image

<pre>docker build -t vip-api -f docker/Dockerfile .</pre>

### Run the Container

<pre>docker run -p 8000:8000 vip-api</pre>

---

## ☁️ Kubernetes Deployment

### Apply Manifests

<pre>kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml</pre>

---

## 📊 MLflow Tracking

### Start MLflow UI:

<pre>mlflow ui</pre>

Open browser: http://127.0.0.1:5000

---

## 🧠 Tech Stack

Python 3.9

Apache Spark

XGBoost

FastAPI

MLflow

Docker & Kubernetes

Pandas, Scikit-learn, Pydantic