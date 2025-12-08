# Encoder API Reference

## Overview  
`Encoder` is a categorical data transformer that converts string or categorical columns into numerical representations using either **label encoding** or **one-hot encoding**. It inherits from `BaseTransformer` and supports:

- `fit`, `transform`, and `fit_transform`
- Input validation for pandas DataFrames  
- Recording fitted parameters  
- Saving and loading state  
- Optional logging via `BaseTransformer`

It learns category mappings during `fit` and applies them during `transform`.

## Constructor  

```python
Encoder(
    method: str = "onehot",
    handle_unseen: str = "ignore",
    name: Optional[str] = None
)
```
## Parameters

| Parameter  | Type | Description |
| ---------  | ---- | ------------ |
| `method`    | `str`  | Encoding method to use. Options: `"label"`, `"onehot"`. |
| `handle_unsern` | `str`  | How to handle unseen categories during transform. Options: `"ignore"`, `"error"`. |

## Supported Encoding Methods 

| Method | Description |
| ------ | ----------- |
| `label` | Converts categories into integer labels. |
| `onehot` | Creates binary columns for each category. |

## Unseen Category Handling

| Mode | Behavior |
| ---- | -------- |
| `ignore` | Unseen values are encoded as `-1` (label) or ignored (onehot). |
| `error` | Raises a `ValueError` when unseen categories appear. |

## Properties

Inherited from `BaseTransformer`.

| Property | Type | Description |
| -------- | ---- | ----------- |
| `is_fitted` | `bool` | Returns `True` after the transformer has been fitted |
| `fitted_params` | `Dict[str, Any]` | Stores learned category mappings. |

## Methods

`fit`

```python
fit(X: pd.DataFrame, y: Optional[pd.Series] = None) -> Encoder
```

Learns unique category values for each categorical column.
- Only columns with object or category dtype are processed.
- Stores learned mappings in:
```python
self._fitted_params["mappings"]
```
Raises `FrozenTransformerError` if the transformer is frozen.

`transform`

```python
transform(X: pd.DataFrame) -> pd.DataFrame
```
Encodes categorical values using mappings learned during `fit`.

#### Behavior by Method:

**Label Encoding**

- Known categories → mapped to integers.
- Unseen categories:
`"ignore"` → replaced with -1
`"error"` → raises ValueError

**One-Hot Encoding**

- Creates one binary column per known category.
- Drops original categorical columns.
- Unseen categories:
`"ignore"` → ignored
`"error"` → raises ValueError
- Raises `NotFittedError` if called before `fit`.

`fit_transform`

```python
fit_transform(X: pd.DataFrame, y: Optional[pd.Series] = None) -> pd.DataFrame
```
Convenience method that performs `fit` followed by `transform`.

`freeze`

```python
freeze() -> None
```

Prevents further calls to `fit`.

`unfreeze`

```python
unfreeze() -> None
```
Allows fitting again after freezing.

`save`

```python
save(filepath: str) -> None
```
Saves the transformer state to disk using `joblib`.

`load`

```python
load(filepath: str) -> Encoder
```
Loads a saved transformer from disk.

`_validate_input` (Inherited)

```python
_validate_input(X: pd.DataFrame, require_same_columns: bool = False) -> pd.DataFrame
```
Ensures input is a pandas DataFrame and optionally checks column consistency.


## Internal Methods

`_fit`

```python
_fit(X: pd.DataFrame, y=None)
```
Finds all unique categories per categorical column and stores their mappings internally.
- For `"label"`: stores `{category: index}`.
- For `"onehot"`: stores `list of categories`.

- `_transform`

```python
_transform(X: pd.DataFrame) -> pd.DataFrame
```
Encodes the DataFrame using stored mappings.
- Applies either label or one-hot encoding
- Handles unseen values based on `handle_unseen`.
- Logs transformation details using `_log()`.

## Exceptions

| Exceptions | When Raised |
| ---------- | ----------- |
| `NotFittedError` | When `transform` is called before `fit`. |
| `FrozenTransformerError` | When `fit` is called after freezing. |
| `ValueError` | If an unsupported method is used or unseen values appear with `handle_unseen="error"`. |

