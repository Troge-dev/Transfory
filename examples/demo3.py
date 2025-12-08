import pandas as pd
import seaborn as sns

from transfory.pipeline import Pipeline
from transfory.missing import MissingValueHandler
from transfory.outlier import OutlierHandler
from transfory.scaler import Scaler
from transfory.insight import InsightReporter

# Note: This demo requires the 'seaborn' package.
# You can install it by running: pip install seaborn

# --- 1. Load a dataset with potential outliers ---
# We'll use seaborn's 'diamonds' dataset. Columns like 'price' and 'carat'
# often have skewed distributions, making them great for demonstrating outlier handling.
print("Loading Diamonds dataset from seaborn...")
df = sns.load_dataset('diamonds')

# For this demo, we'll focus on a few numeric columns and one categorical
df = df[['carat', 'depth', 'table', 'price', 'cut']]

print("=== Original Data Description (Diamonds) ===")
print(df.describe()) # .describe() is great for seeing potential outliers
print("\nMissing values before processing:")
print(df.isnull().sum())

# --- 2. Define a Pipeline including the OutlierHandler ---
reporter = InsightReporter()

pipeline = Pipeline(
    steps=[
        # The diamonds dataset is clean, but we include this for completeness
        ("impute_values", MissingValueHandler(strategy="mean")),
        # Add the new OutlierHandler to cap extreme values using the IQR method
        ("handle_outliers", OutlierHandler(method="iqr", factor=1.5)),
        # Scale the capped numeric features
        ("scale_numeric", Scaler(method="zscore"))
    ],
    logging_callback=reporter.get_callback()
)

# --- 3. Run the Pipeline and Display Results ---
processed = pipeline.fit_transform(df)

print("\n\n=== Processed Data Description ===")
# .describe() is useful again to see how the distributions have changed (e.g., min/max values)
print(processed.describe())

print("\n\n=== Transformation Report ===")
print(reporter.summary())