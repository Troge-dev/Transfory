# API Reference

This document explains the **main classes and functions** of Transfory, including their **parameters, behavior, and usage.**

## MissingValueHandler

**Purpose:**
*  This class handles missing values `(NaN)` in a pandas DataFrame. It can automatically fill missing data using different strategies or a constant value. This is useful for cleaning datasets before analysis or machine learning.

**Parameters:**
| Parameter   | Type  | Default | Description |
|------------|-------|---------|-------------|
| strategy   | str   | "mean"  | Method to handle missing values: "mean", "median", "mode", "constant" |
| fill_value | Any   | None    | Custom value to fill missing entries. Required if strategy="constant" |
| name       | str   | None    | Optional name for the transformer (used for logging and representation) |

* `strategy`: `"mean"`, "median", `"mode"`, `"drop"` - how missing values are handled.
* `fill_value`: custom value to fill missing data (optional)

## Encoder
- method: label, onehot

## Scaler
- method: minmax, zscore
