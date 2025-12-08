# Transfory

Transfory is an educational, object-oriented data transformation toolkit for Python. While libraries like scikit-learn and pandas are powerful, Transfory focuses on **explainability, traceability, and educational clarity**. It's designed to help data science students and beginners understand not just *what* a transformation does, but *how* and *why* it affects their data.

## Purpose

Data preprocessing is one of the hardest parts for beginners in data science and machine learning. Transfory is useful because it:

*  Automates repetitive preprocessing tasks
*  Uses Object-Oriented Programming (OOP) for clean and reusable code
*  Helps students understand what happens to their data through the Transformation Insight Engine
*  Makes preprocessing easier, faster, and more educational

## Key Features: Beyond the Transformation

Transfory's core mission is to make the "black box" of data preprocessing transparent. It achieves this through:

*   **Human-Readable Reports**: Generate clear, step-by-step summaries of the entire transformation process. See exactly which columns were imputed, how an encoder was fitted, and what new features were created.
*   **Traceability**: The `InsightReporter` provides step-by-step logs, creating a complete audit trail of your data's journey through the pipeline.
*   **Data Snapshots**: Get before-and-after insights into your data's shape and structure at every stage, helping you visualize the impact of each transformer.
*   **Modular OOP Design**: Built with clean, object-oriented principles, making it easy to understand, extend, and learn from.

## Core Modules

- **Missing Value Imputation**: Handle `NaN` values with strategies like mean, median, or constant.
- **Encoding**: Convert categorical features using label or one-hot encoding.
- **Scaling**: Normalize numerical features with Min-Max or Z-score scaling.
- **Feature Generation**: Automatically create polynomial and interaction features.
- **Pipeline Automation**: Chain all your transformation steps into a single, reusable object.
- **Insight Reporting**: The engine that powers Transfory's explainability.

## Support and Help

Users can get support through:

*  The project README documentation
*  The API reference inside the /docs folder
*  The example notebooks found in the /examples directory
*  The GitHub Issues page for bug reports and feature requests

 ## Project Maintainer and Contributors

Transfory is maintained and developed by a team of five student contributors as part of an Object-Oriented Programming final project. Each member contributes through coding, documentation, testing, and project coordination.
