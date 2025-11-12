# tests/test_insight.py
from transfory.base import ExampleScaler
from transfory.pipeline import Pipeline
from transfory.insight import InsightReporter
import pandas as pd

# === STEP 1: create dummy data ===
df = pd.DataFrame({
    "age": [20, 30, 40],
    "income": [1000, 2000, 3000]
})

# === STEP 2: create InsightReporter ===
reporter = InsightReporter()

# === STEP 3: attach reporter to a transformer ===
scaler = ExampleScaler(logging_callback=reporter.log_event)

# === STEP 4: build a pipeline ===
pipe = Pipeline([("scale", scaler)], logging_callback=reporter.log_event)

# === STEP 5: run some operations ===
pipe.fit(df)
transformed = pipe.transform(df)

# === STEP 6: view insights ===
print("\n===== INSIGHT REPORT =====")
print(reporter.summary())
