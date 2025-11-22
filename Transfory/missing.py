import pandas as pd
import numpy as np
from .base import Transformer

class MissingValueHandler(Transformer):
    def __init__(self, strategy="mean", fill_value=None):
        self.strategy = strategy
        self.fill_value = fill_value
        self._fill_values = {}   # stored during fit()

    def fit(self, X: pd.DataFrame):
        if self.strategy in ["mean", "median", "mode"]:
            for col in X.columns:
                if X[col].isna().sum() == 0:
                    continue

                if self.strategy == "mean":
                    self._fill_values[col] = X[col].mean()
                elif self.strategy == "median":
                    self._fill_values[col] = X[col].median()
                elif self.strategy == "mode":
                    self._fill_values[col] = X[col].mode().iloc[0]

        elif self.strategy == "constant":
            for col in X.columns:
                self._fill_values[col] = self.fill_value

        elif self.strategy == "drop":
            pass  # no stats needed

        return self

    def transform(self, X: pd.DataFrame):
        X = X.copy()

        if self.strategy == "drop":
            return X.dropna()

        for col, val in self._fill_values.items():
            X[col] = X[col].fillna(val)

        return X

    def __repr__(self):
        return f"MissingValueHandler(strategy='{self.strategy}')"
