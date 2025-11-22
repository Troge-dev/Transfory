import pandas as pd
from itertools import combinations
from .base import Transformer

class FeatureGenerator(Transformer):
    def __init__(self, degree=2, include_interactions=True):
        self.degree = degree
        self.include_interactions = include_interactions
        self.columns_ = []

    def fit(self, X: pd.DataFrame):
        self.columns_ = list(X.select_dtypes(include="number").columns)
        return self

    def transform(self, X: pd.DataFrame):
        X = X.copy()

        # Polynomial features
        for col in self.columns_:
            for p in range(2, self.degree + 1):
                X[f"{col}^p{p}"] = X[col] ** p

        # Interaction terms
        if self.include_interactions:
            for col1, col2 in combinations(self.columns_, 2):
                X[f"{col1}_x_{col2}"] = X[col1] * X[col2]

        return X

    def __repr__(self):
        return f"FeatureGenerator(degree={self.degree})"
