# BaseTransformer API Reference

## Overview

`BaseTransformer` is the abstract base class for all transformers in **Transfory**. It provides a standard interface for:

* `fit`, `transform`, and `fit_transform` methods  
* Input validation for pandas DataFrames  
* Recording fitted parameters  
* Saving/loading transformer state  
* Optional logging for tracking transformations  

All custom transformers in Transfory should inherit from `BaseTransformer`.

---

## Exceptions

* `NotFittedError` – Raised if you call `transform` before `fit`.  
* `FrozenTransformerError` – Raised if you try to `fit` a frozen transformer.  

---

## Constructor

```python
BaseTransformer(
    name: Optional[str] = None,
    logging_callback: Optional[Callable[[str, Dict[str, Any]], None]] = None
)
```

---

## Parameters

| Property        | Type   | Description                                      |
| --------------- | ------ | ------------------------------------------------ |
| `is_fitted`     | `bool` | Returns `True` if transformer has been fitted.   |
| `fitted_params` | `dict` | Dictionary of parameters learned during fitting. |

---

## Methods

* `fit`
```python
fit(X: pd.DataFrame, y: Optional[pd.Series] = None) -> BaseTransformer
```
*Fits the transformer to X (and optionally y).*
Raises `FrozenTransformerError` if transformer is frozen.

* `transform`
```python
transform(X: pd.DataFrame) -> pd.DataFrame
```

*Transforms the data using the learned parameters.*
Raises `NotFittedError` if transformer is not fitted.

* `fit_transform`
```python
fit_transform(X: pd.DataFrame, y: Optional[pd.Series] = None) -> pd.DataFrame
```
*Convenience method that calls *`fit`* then *`transform`*.*

* `freeze`/`unfreeze`
```python
Convenience method that calls fit then transform.
```
Prevents further calls to `fit`.
```python
unfreeze() -> None
```
Allows `fit` again after freezing.

* `save`/`load`
```python
save(filepath: str) -> None
```
Saves the transformer to disk using `joblib`.
```python
load(filepath: str) -> BaseTransformer
```
Loads a transformer from disk.

## Other Notes

* `_validate_input` - Internal method to ensure input is a DataFrame and columns match.
* `_log` - Internal method to send logs to `logging_callback`.
* `__repr__` - Returns a readable summary of the transformer and its fitted parameters.
* `__eq__` - Compares transformers by class, name, and fitted parameters.
* `__len__` - Returns the number of stored fitted parameters.
