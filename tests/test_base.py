# tests/test_base.py
from transfory.base import ExampleScaler
import pandas as pd

def test_example_scaler():
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4, 5, 6]
    })

    scaler = ExampleScaler()
    result = scaler.fit_transform(df)

    print("✅ Test Passed — ExampleScaler works!")
    print("Original DataFrame:\n", df)
    print("Scaled DataFrame:\n", result)

if __name__ == "__main__":
    test_example_scaler()