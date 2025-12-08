from __future__ import annotations
import pandas as pd
import re
import json
from datetime import datetime
from typing import Any, Dict, List, Optional


class InsightReporter:
    """
    Collects and summarizes events emitted by transformers.

    The InsightReporter acts as a lightweight event logger.
    Each transformer calls it via `logging_callback(name, payload)`,
    and the reporter records what transformations were performed.

    Example usage
    -------------
    >>> reporter = InsightReporter()
    >>> callback = reporter.get_callback()
    >>> scaler = ExampleScaler(logging_callback=callback)
    >>> scaler.fit_transform(df)
    >>> print(reporter.summary())
    """

    def __init__(self):
        # Store logs as list of dicts
        self._logs: List[Dict[str, Any]] = []
        self._start_time: datetime = datetime.now()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def get_callback(self):
        """
        Returns a callable that transformers can use for logging.
        This allows the reporter to be plugged into a pipeline easily.
        """
        def _callback(step_name: str, payload: Dict[str, Any]) -> None:
            self.log_event(step_name, payload)
        return _callback

    def log_event(self, step_name: str, payload: Dict[str, Any]) -> None:
        """
        Append a transformation event to the log.
        Automatically timestamps each entry.
        """
        # Unpack the received payload for richer, more structured logs.
        event = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "step": step_name,
            **payload,
        }
        self._logs.append(event)

    def _format_log_entry(self, log: Dict[str, Any]) -> str:
        """Generates a human-readable explanation for a single log entry."""
        step_name = log.get("step", "Unknown Step")
        event = log.get("event", "unknown")
        details = log.get("details", {})
        # Get the original transformer name for display, and a lowercase version for logic.
        display_transformer_name = log.get("transformer_name", step_name)
        logic_transformer_name = display_transformer_name.lower()
        config = log.get("config", {})

        # Default message
        explanation = f"Step '{step_name}' ({display_transformer_name}) completed a '{event}' event."
        if step_name.lower() == logic_transformer_name:
             explanation = f"Step '{step_name}' completed a '{event}' event."

        # --- Custom Explanations for Different Transformers ---

        # MissingValueHandler
        if "missingvaluehandler" in logic_transformer_name and event == "fit":
            cols = self._get_fitted_columns(details, "fill_values")
            if cols:
                strategy = config.get("strategy", "unknown")
                return f"Step '{step_name}' (MissingValueHandler) fitted. Will use '{strategy}' on {len(cols)} column(s): {list(cols)}."
            return f"Imputer '{step_name}' fitted, but no missing values were found to handle."

        # Encoder
        if "encoder" in logic_transformer_name and event == "fit":
            params = details.get("fitted_params", {})
            mappings = params.get("mappings", {})
            if mappings:
                cols = list(mappings.keys()) # Mappings are dicts of {col: mapping}
                method = config.get("method", "unknown")
                return f"Step '{step_name}' (Encoder) fitted. Will apply '{method}' encoding to {len(cols)} column(s): {cols}."
            return f"Encoder '{step_name}' fitted, but no categorical columns were found to encode."

        # Scaler
        if "scaler" in logic_transformer_name and event == "fit":
            cols = self._get_fitted_columns(details, "columns")
            if cols:
                method = config.get("method", "unknown")
                return f"Step '{step_name}' (Scaler) fitted. Will apply '{method}' scaling to {len(cols)} column(s): {cols}."
            return f"Scaler '{step_name}' fitted, but no numeric columns were found to scale."

        # FeatureGenerator
        if "featuregenerator" in logic_transformer_name and event == "transform":
            new_features = details.get("new_features_created", [])
            if new_features:
                return f"Step '{step_name}' (FeatureGenerator) created {len(new_features)} new feature(s), including '{new_features[0]}'..."
            return f"Feature Generator '{step_name}' created 0 new features."

        return explanation

    def _get_fitted_columns(self, details: Dict[str, Any], param_key: str) -> List[str]:
        """Helper to extract fitted column names from a log's details."""
        params = details.get("fitted_params", {})
        values = params.get(param_key, {})
        if isinstance(values, dict):
            return list(values.keys())
        if isinstance(values, (list, pd.Index)):
            return list(values)
        return []

    def summary(self, as_dataframe: bool = False) -> Any:
        """
        Summarize logged transformations in a readable format.

        Parameters
        ----------
        as_dataframe : bool
            If True, return a pandas.DataFrame. Otherwise, return a formatted string.
        """
        if not self._logs:
            return "No transformation logs recorded."

        if as_dataframe:
            return pd.DataFrame(self._logs)

        # Format as readable text
        lines = [
            f"=== Transfory Insight Report ===",
            f"Session started: {self._start_time.strftime('%Y-%m-%d %H:%M:%S')}",
            f"Total steps logged: {len(self._logs)}",
            "",
        ]
        for log in self._logs:
            lines.append(f"[{log['timestamp']}] {self._format_log_entry(log)}")
        return "\n".join(lines)

    def clear(self) -> None:
        """Reset all stored logs."""
        self._logs.clear()

    def export(self, filepath: str, format: str = "json") -> None:
        """
        Export logs to a file (JSON or CSV).

        Parameters
        ----------
        filepath : str
            Destination path.
        format : str
            "json" or "csv"
        """
        if not self._logs:
            raise ValueError("No logs to export.")

        if format == "json":
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(self._logs, f, indent=2)
        elif format == "csv":
            df = pd.DataFrame(self._logs)
            df.to_csv(filepath, index=False)
        else:
            raise ValueError("Unsupported format. Use 'json' or 'csv'.")

    def __repr__(self) -> str:
        return f"<InsightReporter logs={len(self._logs)}>"
