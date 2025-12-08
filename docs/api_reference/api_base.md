# BaseTransformer API Reference

## Overview

`BaseTransformer` is the abstract base class for all transformers in **Transfory**. It provides a standard interface for:

* `fit`, `transform`, and `fit_transform` methods  
* Input validation for pandas DataFrames  
* Recording fitted parameters  
* Saving/loading transformer state  
* Optional logging for tracking transformations  

All custom transformers in Transfory should inherit from `BaseTransformer`. 

## Constructor

```python
BaseTransformer(name: Optional[str] = None, logging_callback: Optional[Callable[[str, Dict[str, Any]], None]] = None)
```
## Parameters

* `name` (Optional[str]): Human-readable name for the transformer. Defaults to class name.
* `logging_callback` (Optional[callable]): Function called after `fit` or `transform` to log events. Signature: `(step_name: str, details: dict)`

## Properties

| Property        | Type   | Description                                      |
| --------------- | ------ | ------------------------------------------------ |
| `is_fitted`     | `bool` | Returns `True` if transformer has been fitted.   |
| `fitted_params` | `Dict[str, Any]` | Dictionary of parameters learned during fitting. |

## Methods

`fit`
```python
fit(X: pd.DataFrame, y: Optional[pd.Series] = None) -> BaseTransformer
```
*Fits the transformer to X (and optionally y).*
Raises `FrozenTransformerError` if transformer is frozen.

`transform`
```python
transform(X: pd.DataFrame) -> pd.DataFrame
```

*Transforms the data using the learned parameters.*
Raises `NotFittedError` if transformer is not fitted.

`fit_transform`
```python
fit_transform(X: pd.DataFrame, y: Optional[pd.Series] = None) -> pd.DataFrame
```
*Convenience method that calls *`fit`* then *`transform`*.*

`freeze`/`unfreeze`
```python
Convenience method that calls fit then transform.
```
Prevents further calls to `fit`.
```python
unfreeze() -> None
```
Allows `fit` again after freezing.

`save`/`load`
```python
save(filepath: str) -> None
```
Saves the transformer to disk using `joblib`.
```python
load(filepath: str) -> BaseTransformer
```
Loads a transformer from disk.

`_validate_input`
```python
_validate_input(X: pd.DataFrame, require_same_columns: bool = False) -> pd.DataFrame
```
Ensures X is a pandas DataFrame.
Optionally checks that columns match those seen during `fit`.

## Exceptions

* `NotFittedError` – Raised if you call `transform` before `fit`.  
* `FrozenTransformerError` – Raised if you try to `fit` a frozen transformer. 

