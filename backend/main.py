from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import joblib
import pandas as pd
import xgboost  # Import XGBoost before loading the model
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title="Churn Prediction API")

# CORS (for frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Load model (ROBUST PATH)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "churn_classifier.pkl"

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Model loading failed: {e}")

# -----------------------------
# Feature list (MUST match training)
# -----------------------------
FEATURES = [
    "total_sessions",
    "total_orders",
    "avg_order_value",
    "days_since_last_purchase",
    "support_tickets",
    "returns_requested",
    "bounce_rate",
    "conversion_rate",
    "cart_abandonment_rate",
    "customer_lifetime_value",
    "engagement_score"
]

# Set feature names on the model if it's an XGBoost model
if hasattr(model, 'get_booster'):
     try:
          model.get_booster().feature_names = FEATURES
     except:
          pass
# -----------------------------
# Health check endpoint
# -----------------------------
@app.get("/")
def health_check():
    return {"status": "API running successfully"}

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict")
def predict(data: dict):
    try:
        # Validate input
        missing = [f for f in FEATURES if f not in data]
        if missing:
            raise HTTPException(
                status_code=400,
                detail=f"Missing features: {missing}"
            )

        # Convert all values to float to avoid type errors
        try:
            data_floats = {f: float(data[f]) for f in FEATURES}
        except (ValueError, TypeError) as e:
            logger.error(f"Data conversion error: {str(e)}, data={data}")
            raise HTTPException(status_code=400, detail=f"Invalid data types: {str(e)}")

        # Create DataFrame
        # Create DataFrame from dict directly to preserve feature names
        import numpy as np
        input_df = pd.DataFrame([data_floats])
        # Ensure columns are in the correct order
        input_df = input_df[FEATURES]
        logger.info(f"Input data shape: {input_df.shape}, dtypes: {input_df.dtypes}")
        logger.info(f"Feature names: {list(input_df.columns)}")

        # Predict

        # Convert to numpy to avoid feature name validation issues
        X = np.array([[data_floats[f] for f in FEATURES]])
        prediction = int(model.predict(X)[0])
        probability = float(model.predict_proba(X)[0][1])
        return {
            "churn_prediction": "High Risk" if prediction == 1 else "Low Risk",
            "confidence_percent": round(probability * 100, 2)
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
