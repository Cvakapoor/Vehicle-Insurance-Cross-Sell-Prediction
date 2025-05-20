import pandas as pd
import mlflow.sklearn

def predict_and_generate_submission():
    df_test = pd.read_csv("data/processed_test.csv")
    ids = pd.read_csv("data/test.csv")["id"]

    if "id" in df_test.columns:
        df_test = df_test.drop(columns=["id"])

    model = mlflow.sklearn.load_model("models:/model/latest")
    predictions = model.predict(df_test)

    submission = pd.DataFrame({
        "id": ids,
        "Response": predictions.astype(int)
    })

    submission.to_csv("submission.csv", index=False)
    print("✅ submission.csv saved!")

if __name__ == "__main__":
    predict_and_generate_submission()