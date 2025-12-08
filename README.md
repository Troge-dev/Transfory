# Transfory

Transfory is an educational, object-oriented data transformation toolkit for Python. While libraries like scikit-learn and pandas are powerful, Transfory focuses on **explainability, traceability, and educational clarity**. It's designed to help data science students and beginners understand not just *what* a transformation does, but *how* and *why* it affects their data.

Transfory is especially useful for data science students, beginners, and anyone learning data preprocessing, because it shows clear explanations of every step in the data transformation process.

## Purpose

Data preprocessing is one of the most difficult steps for beginners in data science and machine learning. Transfory is designed to make this process easier, faster, and educational. It helps users by:

*  Automates repetitive preprocessing tasks
*  Uses Object-Oriented Programming (OOP) for clean and reusable code
*  Helps students understand what happens to their data through the Transformation Insight Engine
*  Makes preprocessing easier, faster, and more educational

## Key Features: Beyond the Transformation

Transfory's core mission is to make the *"black box"* of data preprocessing transparent. It achieves this through:

*   **Human-Readable Reports**: Every transformation produces a detailed summary that shows what changes were made, such as which missing values were filled, which columns were encoded, or which features were created.
*   **Traceability**: The `InsightReporter` keeps a complete log of all steps in the pipeline. Users can track exactly what happens at each stage.
*   **Data Snapshots**: Users can see the data before and after every transformation, making it easy to visualize the effect of each step.
*   **Modular OOP Design**: Built with clean, object-oriented principles, making it easy to understand, extend, and learn from.

## Core Modules

- **Missing Value Imputation**: Handle `NaN` values with strategies like mean, median, or constant.
- **Encoding**: Converts categorical data into numbers using label encoding or one-hot encoding.
- **Scaling**: Normalize numerical features with Min-Max or Z-score scaling.
- **Feature Generation**: Automatically creates new features by generating polynomials or interactions between existing features.
- **Pipeline Automation**: Combines multiple transformation steps into a single reusable pipeline, making workflows consistent and easy to run on multiple datasets.
- **Insight Reporting**: The engine that powers Transfory's explainability.

## Support and Help

Users can get support through:

*  The project README documentation
*  The API reference inside the '/docs' folder
*  The GitHub Issues page for bug reports and feature requests

 ## Project Maintainer and Contributors

Transfory is maintained and developed by a team of five student contributors as part of an Object-Oriented Programming final project. Each member contributes through coding, documentation, testing, and project coordination.
