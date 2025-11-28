import pandas as pd
import numpy as np

# Import your transformers (adjust the import paths as needed)
from transfory.encoder import Encoder
from transfory.featuregen import FeatureGenerator
from transfory.missing import MissingValueHandler
from transfory.scaler import Scaler


# -----------------------------
# 1) CREATE A SYNTHETIC DATASET
# -----------------------------
df = pd.DataFrame({
    "age": [20, 25, 30, np.nan, 22],
    "income": [50000, 60000, np.nan, 55000, 52000],
    "city": ["Manila", "Cebu", "Manila", "Davao", None],
    "gender": ["M", "F", "F", None, "M"]
})

print("\n=== ORIGINAL DATA ===")
print(df)


# -----------------------------
# 2) MISSING VALUE HANDLER TEST
# -----------------------------
mv = MissingValueHandler(strategy="mean")
mv.fit(df)
df_mv = mv.transform(df)

print("\n=== AFTER MISSING VALUE HANDLER ===")
print(df_mv)


# -----------------------------
# 3) ENCODER TEST
# -----------------------------
enc = Encoder(method="onehot")
enc.fit(df_mv)
df_enc = enc.transform(df_mv)

print("\n=== AFTER ENCODING ===")
print(df_enc)


# -----------------------------
# 4) FEATURE GENERATOR TEST
# -----------------------------
fg = FeatureGenerator(degree=2, include_interactions=True)
fg.fit(df_enc)
df_fg = fg.transform(df_enc)

print("\n=== AFTER FEATURE GENERATION ===")
print(df_fg)


# -----------------------------
# 5) SCALER TEST
# -----------------------------
scaler = Scaler(method="zscore")
scaler.fit(df_fg)
df_scaled = scaler.transform(df_fg)

print("\n=== AFTER SCALING ===")
print(df_scaled)


# -----------------------------
# 6) FINAL SHAPE CHECK
# -----------------------------
print("\n=== FINAL SHAPE ===")
print(df_scaled.shape)
