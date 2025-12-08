# How to Use Transfory

Welcome to Transfory! This guide will walk you through the basic steps to use the library for cleaning and preparing your data.

## 1. Installation

First, you'll need to install the library from PyPI using pip. Open your terminal and run the following command:

`pip install transfory`

## 2. The Core Idea

The main goal of Transfory is to apply a series of transformations to your data while keeping track of every change. You do this by building a `Pipeline` and attaching an `InsightReporter` to it.

## 3. A Step-by-Step Example

Let's walk through a typical use case.

### Step A: Import the Tools

To begin, you'll import the necessary components from the library: the `Pipeline` class, the transformers you need (like `MissingValueHandler`, `Encoder`, and `Scaler`), and the `InsightReporter`. You will also need `pandas` to handle your data.

### Step B: Prepare Your Data

Load or create your data as a pandas DataFrame. This DataFrame can have missing values, categorical columns, and numerical columns that you want to process.

### Step C: Define Your Transformation Pipeline

This is the core of the process. You will create a list of steps, where each step is a tuple containing a unique name and an instance of a transformer.

For example, you might define a pipeline that first handles missing numerical values using the 'mean' strategy, then handles missing categorical values using the 'mode' strategy. After that, it could convert categorical columns into a one-hot encoded format, and finally, scale all numerical features using a Z-score scaler.

When you create your `Pipeline` instance, you will pass this list of steps to it. Crucially, you will also create an `InsightReporter` and pass its callback function to the pipeline. This hooks the reporter into every step.

### Step D: Run the Pipeline

With your pipeline defined, you can now process your data with a single command: `fit_transform`. This method will execute each step in your pipeline sequentially on your DataFrame. The output will be a new, fully transformed DataFrame.

### Step E: See What Happened

This is where Transfory shines. After running the pipeline, you can ask the `InsightReporter` for a `summary`. It will print a human-readable report detailing every action that was taken: which columns were imputed, what values were used, how categorical columns were encoded, and which columns were scaled. This provides a complete audit trail of your data's transformation.

### Step F: Save Your Trained Pipeline

After you have fitted the pipeline on your training data, you can save the entire pipeline object to a file using its `save` method. This saves all the learned parameters, like the means, modes, and scaling factors, that are necessary for consistent transformation.

### Step G: Reuse the Pipeline on New Data

Later, when you have new, unseen data that needs to be prepared for your model, you can load the saved pipeline using the `load` method.

Instead of fitting again, you will just call the `transform` method on your new data. The loaded pipeline will apply the exact same transformations using the parameters it learned from the original training data, ensuring consistency and preventing data leakage.

And that's it! You've successfully used Transfory to build a reproducible, explainable, and robust data preprocessing workflow.