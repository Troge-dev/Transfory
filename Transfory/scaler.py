import pandas as pd
from .base import Transformer

class Scaler(Transformer):
    def __init__(self, method="minmax"):
        self.method = method
        self.params = {}

    def fit(self, X: pd.DataFrame):
        num_cols = X.select_dtypes(include="number").columns
        
        for col in num_cols:
            if self.method == "minmax":
                self.params[col] = (X[col].min(), X[col].max())
            elif self.method == "zscore":
                self.params[col] = (X[col].mean(), X[col].std())

        return self

    def transform(self, X: pd.DataFrame):
        X = X.copy()

        for col, p in self.params.items():
            if self.method == "minmax":
                mn, mx = p
                X[col] = (X[col] - mn) / (mx - mn + 1e-9)

            elif self.method == "zscore":
                mean, std = p
                X[col] = (X[col] - mean) / (std + 1e-9)

        return X

    def __repr__(self):
        return f"Scaler(method='{self.method}')"
