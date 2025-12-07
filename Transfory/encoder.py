import pandas as pd
from typing import Optional
from .base import BaseTransformer

class Encoder(BaseTransformer):
    def __init__(self, method="onehot", name: Optional[str] = None):
        super().__init__(name=name or f"Encoder(method='{method}')")
        
        supported_methods = ["label", "onehot"]
        if method not in supported_methods:
            raise ValueError(f"Method '{method}' is not supported. Use one of {supported_methods}.")
            
        self.method = method
        self._fitted_params = {"mappings": {}}

    def _fit(self, X: pd.DataFrame, y=None):
        self._fitted_params["mappings"] = {}
        cat_cols = X.select_dtypes(include=["object", "category"]).columns
        for col in cat_cols:
            # Store unique categories found during fitting
            unique_cats = X[col].dropna().unique()
            if self.method == "label":
                self._fitted_params["mappings"][col] = {cat: i for i, cat in enumerate(unique_cats)}
            elif self.method == "onehot":
                self._fitted_params["mappings"][col] = list(unique_cats)

    def _transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        mappings = self._fitted_params.get("mappings", {})
        original_cols = X.columns.tolist()

        if self.method == "label":
            for col, mapping in mappings.items():
                if col in X.columns:
                    # Map known categories, fill others with -1 (for unknown)
                    X[col] = X[col].map(mapping).fillna(-1).astype(int)
            self._log("transform", {"columns_encoded": list(mappings.keys())})

        elif self.method == "onehot":
            for col, known_cats in mappings.items():
                if col in X.columns:
                    for cat in known_cats:
                        # Create column for each known category
                        X[f"{col}_{cat}"] = (X[col] == cat).astype(int)
                    # Drop original column after encoding
                    X.drop(columns=[col], inplace=True)
            
            new_cols = [c for c in X.columns if c not in original_cols]
            self._log("transform", {
                "input_shape": (X.shape[0], len(original_cols)),
                "new_columns_added": new_cols,
                "output_shape": X.shape
            })

        return X

    def __repr__(self):
        return f"Encoder(method='{self.method}')"
