# MissingValueHandler API Reference

## Overview  
`MissingValueHandler` is a transformer used to handle missing values in a pandas DataFrame using different imputation strategies. It inherits from `BaseTransformer` and fully supports:

- `fit`, `transform`, and `fit_transform`
- Input validation for pandas DataFrames  
- Recording fitted parameters  
- Saving and loading state  
- Optional logging via `BaseTransformer`

It computes replacement values during `fit` and applies them during `transform`.

## Constructor  

```python
MissingValueHandler(
    strategy: str = "mean",
    fill_value: Any = None,
    name: Optional[str] = None
)
```
## Parameters

| Parameter  | Type | Description |
| ---------  | ---- | ------------ |
| `srategy`    | `str`  | Strategy used to fill missing values. Options: `"mean"`, `"median"`, `"mode"`, `"constant"` |
| `fill_value` | `Any`  | Required only when `strayegy="constant"`. This value will replace missing entries. |

## Supported Strategies

| Strategy | Description |
| -------- | ----------- |
| mean     | Replaces missing values using the column mean (numeric only). |
| median   | Replaces missing values using ghe column median (numeric only). |
| mode     | Replaces missing calues using the most frequent value (numeric or categorical). |
| constant | Replaces missing values using `fill_values`. |

## Properties

Inherited from `BaseTransformer`

| Property | Type | Description |
| -------- | ---- | ----------- |
| `is_fitted` | `bool` | Returns `True` after the transformer has been fitted |
| `fitted_params` | `Dict[str, Any]` | Stores learned imputation values (`fill_valuee`) |

## Methods

* `fit`

```python
fit(X: pd.DataFrame, y: Optional[pd.Series] = None) -> MissingValueHandler
```
Computes the replacement values for each column based on the selected strategy. 
- Only columns with missing values are processed.
- Learned values are stored in:

```python
self._fitted_params["fill_values"]
```
- Raises `FrozenTransformerError` if the transformer is frozen.

* `transform`

```python
transform(X: pd.DataFrame) -> pd.DataFrame
```
Fills missing values using the values learned during `fit`.
- Uses `DataFrams.fillna()` with a dictionary of values.
- Raised `NotFittedError` if called before `fit`.

* `fit_transform`

```python
fit_transform(X: pd.DataFrame, y: Optional[pd.Series] = None) -> pd.DataFrame
```

Convenience method that performs `fit` followed by `transform`.

* `freeze'
  
```python
freeze() -> None
```
Prevents further calls to `fit`.

* `unfreeze`

```python
unfreeze() -> None
```
Allows fitting again after freezing.

* `save`

```
save(filepath: str) -> None
```
Saves the transformer state to disk using `joblib`.

* `load`

```python
load(filepath: str) -> MissingValueHandler
```
Loads a saved transformed from disk

* `_validate_input` (Inherited)

```python
_validate_input(X: pd.DataFrame, require_same_columns: bool = False) -> pd.DataFrame
```
Ensures inout is a pandan DataFrame and optionally checks column consistency.

## Internal Methods

* `_fit`

```python
_fit(X: pd.DataFrame, y=None)
```
Computes fill values per column based on the chosen strategy and stores them initially in:
```python
self._fill_values
```

* `_transform`

```python
_transform(X: pd.DataFrame) -> pd.DataFrame
```
Applies the stored `fill_values` to replace missing values in the DataFrame.

## Exceptions

| Exception | When Raised |
| --------- | ----------- |
| `NotFittedError` | When `transform` is called before `fit`. |
| `FrozenTransformedError` | When `fit` is called after `freezing`. |
| `ValueError` | If an unsupported strategy is used or `fill_value` is missing for `"constant"`. |
