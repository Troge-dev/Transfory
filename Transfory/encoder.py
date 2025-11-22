import pandas as pd
from .base import Transformer

class Encoder(Transformer):
    def __init__(self, method="label"):
        self.method = method
        self.categories_ = {}

    def fit(self, X: pd.DataFrame):
        cat_cols = X.select_dtypes(include=["object", "category"]).columns
        
        for col in cat_cols:
            self.categories_[col] = list(X[col].dropna().unique())

        return self

    def transform(self, X: pd.DataFrame):
        X = X.copy()

        if self.method == "label":
            for col, cats in self.categories_.items():
                mapping = {cat: i for i, cat in enumerate(cats)}
                X[col] = X[col].map(mapping).fillna(-1)

        elif self.method == "onehot":
            for col, cats in self.categories_.items():
                for cat in cats:
                    X[f"{col}_{cat}"] = (X[col] == cat).astype(int)
                X.drop(columns=[col], inplace=True)

        return X

    def __repr__(self):
        return f"Encoder(method='{self.method}')"
