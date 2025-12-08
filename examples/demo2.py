import sys
import os
# Add the project root to the path to allow importing 'transfory'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
import seaborn as sns

from transfory.pipeline import Pipeline
from transfory.missing import MissingValueHandler
from transfory.encoder import Encoder
from transfory.scaler import Scaler
from transfory.featuregen import FeatureGenerator
from transfory.insight import InsightReporter

# Note: This demo requires the 'seaborn' package.
# You can install it by running: pip install seaborn
# --- 1. Load a different real-world dataset ---
# We'll use seaborn's built-in Penguins dataset. It's a modern dataset
# with missing values and a good mix of data types.
print("Loading Penguins dataset from seaborn...")
df = sns.load_dataset('penguins')

# For this demo, we'll select a good mix of columns.
# Note: 'species' is often the target variable, but we'll include it in the transformation for this demo.
df = df[['species', 'island', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g', 'sex']]

print("=== Original Data (Penguins) ===")
print(df.head())
print("\nMissing values before processing:")
print(df.isnull().sum())

# --- 2. Define the Transformation Pipeline with an InsightReporter ---
reporter = InsightReporter()

pipeline = Pipeline(
    steps=[
        ("impute_all", MissingValueHandler(strategy="mean")), # 'mean' applies mean to numeric and mode to categoric
        ("encode_cats", Encoder(method="onehot")),
        ("generate_features", FeatureGenerator(degree=2, include_interactions=False)), # Just create polynomial features this time
        ("scale_numeric", Scaler(method="zscore"))
    ],
    logging_callback=reporter.get_callback()
)

# --- 3. Run the Pipeline and Display Results ---
processed = pipeline.fit_transform(df)

print("\n\n=== Processed Data ===")
pd.set_option('display.max_columns', None) # Show all columns
print(processed.head())

print("\n\n=== Transformation Report ===")
print(reporter.summary())