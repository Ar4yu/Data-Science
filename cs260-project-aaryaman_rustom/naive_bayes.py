import os
import argparse
import joblib
import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

def parse_args():
    parser = argparse.ArgumentParser(
        description="Train a Gaussian Naive Bayes on the Pima diabetes dataset."
    )
    parser.add_argument(
        "--data-path",
        type=str,
        required=True,
        help="Path to the diabetes CSV file"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="reports",
        help="Directory to save the model"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    # 1) Load
    df = pd.read_csv(args.data_path)
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    # 2) Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3) Train & Evaluate
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    y_pred = nb.predict(X_test)

    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # 4) Save model
    model_path = os.path.join(args.output_dir, "naive_bayes.joblib")
    joblib.dump(nb, model_path)
    print(f"Saved Naive Bayes model to {model_path}")

if __name__ == "__main__":
    main()
