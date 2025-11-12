"""
transfory/insight.py

InsightReporter — the educational heart of Transfory.
Collects transformation logs from each step and generates
a clear, human-readable report of what happened to the data.

Author: [Your Name]
"""

from __future__ import annotations
import pandas as pd
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
        event = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "step": step_name,
            "event": payload.get("event", "unknown"),
            "details": payload.get("details", {}),
        }
        self._logs.append(event)

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
            lines.append(f"[{log['timestamp']}] Step: {log['step']} | Event: {log['event']}")
            details = log.get("details", {})
            for k, v in details.items():
                lines.append(f"   - {k}: {v}")
            lines.append("")
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
