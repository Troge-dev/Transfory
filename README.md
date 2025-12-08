# Transfory

Transfory is an educational, object-oriented data transformation toolkit for Python. While libraries like scikit-learn and pandas are powerful, Transfory focuses on **explainability, traceability, and educational clarity**. It's designed to help data science students and beginners understand not just *what* a transformation does, but *how* and *why* it affects their data.

## Purpose

Data preprocessing is one of the most difficult steps for beginners in data science and machine learning. Transfory is designed to make this process easier, faster, and educational. It helps users by:

*   Automating repetitive preprocessing tasks
*   Using Object-Oriented Programming (OOP) for clean and reusable code
*   Helping students understand what happens to their data through the Transformation Insight Engine
*   Making preprocessing easier, faster, and more educational

## Key Features

Transfory's core mission is to make the *"black box"* of data preprocessing transparent. It achieves this through:

*   **Human-Readable Reports**: Every transformation produces a detailed summary that shows what changes were made, such as which missing values were filled, which columns were encoded, or which features were created.
*   **Traceability**: The `InsightReporter` keeps a complete log of all steps in the pipeline. Users can track exactly what happens at each stage.
*   **Data Snapshots**: Users can see the data before and after every transformation, making it easy to visualize the effect of each step.
*   **Human-Readable Reports**: Every transformation produces a detailed summary that shows what changes were made, such as which missing values were filled, which columns were encoded, or which features were created.
*   **Traceability**: The `InsightReporter` keeps a complete log of all steps in the pipeline. Users can track exactly what happens at each stage.
*   **Data Snapshots**: Users can see the data before and after every transformation, making it easy to visualize the effect of each step.
*   **Modular OOP Design**: Built with clean, object-oriented principles, making it easy to understand, extend, and learn from.

## Core Modules

*   **Missing Value Imputation**: Handle `NaN` values with strategies like mean, median, or constant.
*   **Encoding**: Converts categorical data into numbers using label encoding or one-hot encoding.
*   **Scaling**: Normalize numerical features with Min-Max or Z-score scaling.
*   **Feature Generation**: Automatically creates new features by generating polynomials or interactions between existing features.
*   **Pipeline Automation**: Combines multiple transformation steps into a single reusable pipeline, making workflows consistent and easy to run on multiple datasets.
*   **Insight Reporting**: The engine that powers Transfory's explainability.

## Installation

Install Transfory directly from PyPI:

```bash
pip install -i https://test.pypi.org/simple/ transfory
```

## Usage Example

Here is a quick example of how to use `Transfory` to process the Titanic dataset, which has a mix of data types and missing values.

```python
import pandas as pd
import seaborn as sns
from transfory.pipeline import Pipeline
from transfory.missing import MissingValueHandler
from transfory.encoder import Encoder
from transfory.scaler import Scaler
from transfory.insight import InsightReporter

# 1. Load a real-world dataset
df = sns.load_dataset('titanic')
df = df[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']]

print("=== Original Data (first 5 rows) ===")
print(df.head())

# 2. Define the Transformation Pipeline with an InsightReporter
reporter = InsightReporter()

pipeline = Pipeline(
    steps=[
        ("impute_numeric", MissingValueHandler(strategy="mean")),
        ("impute_categoric", MissingValueHandler(strategy="mode")),
        ("encode_cats", Encoder(method="onehot")),
        ("scale_numeric", Scaler(method="zscore"))
    ],
    logging_callback=reporter.get_callback()
)

# 3. Run the Pipeline
processed_df = pipeline.fit_transform(df)

print("\n\n=== Processed Data (first 5 rows) ===")
print(processed_df.head())

# 4. See the Transformation Report
print("\n\n=== Transformation Report ===")
print(reporter.summary())
```

The final report clearly explains every action taken, providing a complete audit trail of the preprocessing workflow.

## How Transfory Compares

How does `Transfory` fit into an ecosystem that already includes powerful tools like `scikit-learn` and `pandas`?

### Transfory vs. scikit-learn

*   **scikit-learn's Strength**: `scikit-learn` is the industry standard for machine learning. Its `Pipeline` is highly optimized for performance and integrates with a massive ecosystem of modeling tools.
*   **Transfory's Niche**: **Explainability and Auditing**. While a `scikit-learn` pipeline is efficient, it can be a "black box." It is not designed to easily produce a step-by-step, human-readable report of what happened inside. `Transfory`'s `InsightReporter` is built for exactly this purpose. It tells you which columns were imputed with which values, what categories were encoded, and what scaling parameters were learned.
*   **Verdict**: `Transfory` is not a replacement for `scikit-learn` but a powerful companion for the **development, debugging, and learning phases** of a project. Use it when you need to build confidence in your preprocessing workflow and maintain a clear audit trail.

### Transfory vs. pandas

*   **pandas' Strength**: `pandas` is the ultimate tool for manual data manipulation. You can perform any transformation you can imagine.
*   **Transfory's Niche**: **Structure and Reproducibility**. Performing preprocessing manually with pandas often leads to code that is hard to read, difficult to reproduce, and prone to errors (e.g., accidentally fitting an imputer on test data). `Transfory` enforces a structured, repeatable `fit`/`transform` workflow inside a `Pipeline`, ensuring that the exact same steps are applied to your training and testing data every time.
*   **Verdict**: Use `Transfory` to turn your manual `pandas` operations into a robust, reusable, and self-documenting `Pipeline`.

## Limitations and When to Use Transfory

`Transfory` is designed with specific goals in mind, and its limitations are a direct result of prioritizing clarity and explainability over raw performance.

*   **Performance**: `Transfory` is written in pure Python and operates on pandas DataFrames. For very large datasets (millions of rows), it will be slower than highly optimized libraries like `scikit-learn`.
*   **In-Memory Only**: The library requires datasets to fit into your machine's RAM, as it does not support distributed computing frameworks like Dask or Spark.
*   **Sequential Processing**: The `Pipeline` processes steps one after another. It does not support applying different transformations to different columns in parallel (unlike `scikit-learn`'s `ColumnTransformer`). This makes the reporting simpler and more linear.

**The ideal use case for `Transfory` is during the development, debugging, and educational phases of a project.** It excels when you need to build confidence in your preprocessing steps, generate clear audit trails, and understand the impact of each transformation on your data.

## Support and Help

Users can get support through:

*   The project README documentation
*   The API reference inside the `/docs` folder
*   The GitHub Issues page for bug reports and feature requests

## Project Contributors

Transfory is maintained and developed by a team of five student contributors as part of an Object-Oriented Programming final project. Each member contributes through coding, documentation, testing, and project coordination.

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.
