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
from transfory.insight import InsightReporter

# Note: This demo requires the 'seaborn' package.
# You can install it by running: pip install seaborn
# --- 1. Load a real-world dataset ---
# We'll use seaborn's built-in Titanic dataset. It's great for demos
# because it contains missing values and a mix of data types.
print("Loading Titanic dataset from seaborn...")
df = sns.load_dataset('titanic')

# For this demo, we'll select a wider range of interesting columns
df = df[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']]

print("=== Original Data ===")
print(df.head())
print("\nMissing values before processing:")
print(df.isnull().sum())

# --- 2. Define the Transformation Pipeline with an InsightReporter ---
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

# --- 3. Run the Pipeline and Display Results ---
processed = pipeline.fit_transform(df)

print("\n\n=== Processed Data ===")
# By default, pandas may truncate the output if the DataFrame is large.
# To see all rows, you can uncomment the following line:
# pd.set_option('display.max_rows', None)
print(processed)

print("\n\n=== Transformation Report ===")
print(reporter.summary())