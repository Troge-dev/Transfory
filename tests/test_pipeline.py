"""
tests/test_pipeline.py

Unit tests for the Transfory Pipeline.
Run this file using:
    python -m tests.test_pipeline
"""

import pandas as pd
from transfory.base import ExampleScaler
from transfory.pipeline import Pipeline


def test_pipeline_basic():
    """Basic pipeline test with a single ExampleScaler."""
    df = pd.DataFrame({"A": [1.0, 2.0, 3.0], "B": [10.0, 20.0, 30.0]})
    pipe = Pipeline([
        ("scaler", ExampleScaler())
    ])

    # Fit and transform
    pipe.fit(df)
    df_out = pipe.transform(df)

    assert not df_out.equals(df), "Pipeline output should differ from input after scaling."
    assert pipe.is_fitted, "Pipeline should be marked as fitted."
    print("[PASS] Basic pipeline fit/transform works.")


def test_pipeline_multiple_steps():
    """Test pipeline with multiple ExampleScaler steps."""
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    pipe = Pipeline([
        ("scaler1", ExampleScaler()),
        ("scaler2", ExampleScaler())
    ])

    pipe.fit(df)
    df_out = pipe.transform(df)
    assert isinstance(df_out, pd.DataFrame), "Output should be a DataFrame."
    print("[PASS] Multiple-step pipeline works correctly.")


def test_pipeline_add_remove_steps():
    """Ensure add_step and remove_step methods work."""
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    pipe = Pipeline([
        ("scaler", ExampleScaler())
    ])

    # Add step
    pipe.add_step("scaler2", ExampleScaler())
    assert len(pipe.steps) == 2, "add_step should increase pipeline length."

    # Remove step
    pipe.remove_step("scaler2")
    assert len(pipe.steps) == 1, "remove_step should reduce pipeline length."

    print("[PASS] add_step and remove_step work correctly.")


def test_pipeline_repr():
    """Check string representation."""
    pipe = Pipeline([
        ("scaler", ExampleScaler())
    ])
    rep = repr(pipe)
    assert "Pipeline" in rep, "repr should contain class name."
    print(f"[PASS] __repr__ works: {rep}")


if __name__ == "__main__":
    test_pipeline_basic()
    test_pipeline_multiple_steps()
    test_pipeline_add_remove_steps()
    test_pipeline_repr()
    print("\n✅ All pipeline tests passed!")
