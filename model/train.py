import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

def train_model():
    df = pd.read_csv("data/processed_train.csv")

    X = df.drop("Response", axis=1)
    y = df["Response"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

    model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    mlflow.set_experiment("vehicle-insurance-prediction")
    with mlflow.start_run():
        mlflow.log_params(model.get_params())
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")

    print(f"Model trained. Accuracy: {acc:.4f}")

if __name__ == "__main__":
    train_model()
