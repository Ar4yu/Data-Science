import os
import argparse
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    accuracy_score,
    precision_score,
    recall_score
)
from sklearn.model_selection import train_test_split

def parse_args():
    parser = argparse.ArgumentParser(
        description="Evaluate and visualize Decision Tree & Naive Bayes models."
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
        help="Directory where model files & outputs live"
    )
    return parser.parse_args()

def eval_model(model_file, name, X_test, y_test, out_dir):
    model = joblib.load(model_file)
    y_pred = model.predict(X_test)

    # Some models (NB, tree) have predict_proba
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
    else:
        y_prob = np.zeros_like(y_pred, dtype=float)

    # Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    print(f"{name} — Acc: {acc:.2f}, Prec: {prec:.2f}, Rec: {rec:.2f}")

    # Confusion matrix
    disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred, normalize="true")
    disp.ax_.set_title(f"{name} Confusion Matrix")
    cm_path = os.path.join(out_dir, f"{name}_confusion.png")
    plt.savefig(cm_path, bbox_inches="tight")
    plt.clf()
    print(f"Saved confusion matrix to {cm_path}")

    # ROC curve
    RocCurveDisplay.from_predictions(y_test, y_prob)
    plt.title(f"{name} ROC Curve")
    roc_path = os.path.join(out_dir, f"{name}_roc.png")
    plt.savefig(roc_path, bbox_inches="tight")
    plt.clf()
    print(f"Saved ROC curve to {roc_path}")

def main():
    args = parse_args()
    # Load data & split exactly the same way as training
    df = pd.read_csv(args.data_path)
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Paths to your saved models
    dt_model = os.path.join(args.output_dir, "decision_tree.joblib")
    nb_model = os.path.join(args.output_dir, "naive_bayes.joblib")

    eval_model(dt_model, "DecisionTree", X_test, y_test, args.output_dir)
    eval_model(nb_model, "NaiveBayes", X_test, y_test, args.output_dir)

if __name__ == "__main__":
    main()
