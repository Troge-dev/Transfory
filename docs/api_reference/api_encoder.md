# Encoder API Reference

## Overview  
`Encoder` is a categorical data transformer that converts string or categorical columns into numerical representations using either **label encoding** or **one-hot encoding**. It inherits from `BaseTransformer` and follows the standard `fit → transform` workflow.

## Constructor  

```python
Encoder(
    method="onehot",
    handle_unseen="ignore",
    name=None
)
```
## Parameters

| Parameter  | Type | Default    | Description |
| ---------  | ---- | ---------- | --------|
| `method`   | `str` | `"onehot"` | Encoding method. Options: `"label"`, `"onehot"`.          |
| `handle_unseen` | `str` | `"ignore"` | How to handle unseen categories during transform. Options: `"ignore"`, `"error"`.|
| `name` | `str` or `None` | `None`| Optional custom name of the transformer. |

## Supported Encoding Methods 

#### 1. Label Encoding (`method="label"`)

Each category is converted into a numeric ID.

Example: 
```python
Gender → {"Male": 0, "Female": 1}
```
Unseen values:
- `"ignore"` → converted to `-1`
- `"error"` → raises ValueError

#### 2. One-Hot Encoding (`method="onehot"`)

Creates a new column for each category.

Example:
```python
City → City_Manila, City_Cebu, City_Davao
```
The original column is removed after encoding.

## Methods

#### `fit(X, y=None)`
Learns the unique categories from categorical columns.
- Detects columns with type: `object` or `category`
- Stores mappings in:
```python
self._fitted_params["mappings"]
```

#### `transform(X) → pd.DataFrame`
Applies encoding using the learned mappings.
- Behaviors are `label encoding` and `one-hot encoding`.

#### `fit_transform(X, y=None)`
Shortcut for:
```python
fit(X)
transform(X)
```

## Learned Attributes
| Attribute                    | Description                         |
| ---------------------------- | ----------------------------------- |
| `_fitted_params["mappings"]` | Stores category mappings per column |

## String Representation
```python
repr(encoder)
```
Returns:
```text
Encoder(method='onehot', handle_unseen='ignore')
```

## Example Usage
```python
from transfory.encoder import Encoder
import pandas as pd

df = pd.DataFrame({
    "city": ["Manila", "Cebu", "Davao"],
    "gender": ["M", "F", "M"]
})

enc = Encoder(method="onehot")
enc.fit(df)
df_encoded = enc.transform(df)

print(df_encoded)
```
