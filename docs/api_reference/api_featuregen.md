# FeatureGenerator API Reference

## Overview  
`FeatureGenerator` is a numerical feature engineering transformer that creates:

- **Polynomial features** (e.g., \(x^2, x^3\))
- **Interaction features** (e.g., \(x_1 \times x_2\))

It inherits from `BaseTransformer` and supports:

- `fit`, `transform`, and `fit_transform`
- Input validation for pandas DataFrames  
- Recording fitted parameters  
- Saving and loading state  
- Optional logging via `BaseTransformer`

It selects numeric columns during `fit` and generates new features during `transform`.

---

## Constructor  

```python
FeatureGenerator(
    degree: int = 2,
    include_interactions: bool = True,
    name: Optional[str] = None,
    logging_callback: Optional[callable] = None
)
```

## Paraneters

| Parameter  | Type | Description |
| ---------  | ---- | ------------ |
| `degree`    | `int`  | Maximum polynomial degree to generate. Must be ≥ 2. |
| `include_interactions` | `bool`  | Whether to generate pairwise interaction features. |
| `logging_callback` | Optional[callable] | Optional logging function called after transformations. |

## Generated Future Types

| Feature Type | Description |
| ------------ | ----------- |
| Polynomial Features | Generates powers of each numeric column: `x², x³, ..., x^degree` |
| Interaction Terms | Generates pairwise products: `col1_x_col2` |

## Properties

Inherited from `BaseTransformer`.

| Property | Type | Description |
| -------- | ---- | ----------- |
| `is_fitted` | `bool` | Returns `True` after the transformer has been fitted |
| `fitted_params` | `Dict[str, Any]` | Stores learned parameters, including numeric columns. |

## Methods
## Internal Methods
## Exceptions
