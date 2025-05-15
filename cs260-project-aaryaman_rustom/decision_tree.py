import os
import argparse
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split

def parse_args():
    parser = argparse.ArgumentParser(
        description="Train a Decision Tree on the Pima diabetes dataset."
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
        help="Directory to save the model and tree image"
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

    # 3) Train
    clf = DecisionTreeClassifier(max_depth=15, random_state=42)
    clf.fit(X_train, y_train)

    # 4) Save model
    model_path = os.path.join(args.output_dir, "decision_tree.joblib")
    joblib.dump(clf, model_path)
    print(f"Saved Decision Tree model to {model_path}")

    # 5) Visualize & save
    plt.figure(figsize=(20, 15),dpi=200)
    plot_tree(
        clf,
        feature_names=X.columns,
        class_names=["NoDiabetes", "Diabetes"],
        filled=True
    )
    img_path = os.path.join(args.output_dir, "decision_tree.png")
    plt.savefig(img_path, bbox_inches="tight")
    print(f"Saved tree visualization to {img_path}")

if __name__ == "__main__":
    main()
