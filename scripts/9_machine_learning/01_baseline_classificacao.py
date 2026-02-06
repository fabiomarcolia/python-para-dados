"""01 — Machine Learning: baseline com scikit-learn

Execute na raiz do repo:
    python scripts/08_machine_learning/01_baseline_classificacao.py
"""

from __future__ import annotations

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def main() -> None:
    data = load_breast_cancer(as_frame=True)
    df = data.frame.copy()

    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=5000)
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)

    print("accuracy:", acc)


if __name__ == "__main__":
    main()
