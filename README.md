# Linear Regression Experimentation

A repository for experimenting with various linear regression models and building an interactive project to visualize and analyze model performance.

## About

This project focuses on building, experimenting with, and visualizing linear regression models, including **basic Linear Regression**, **Lasso Regression**, **Ridge Regression**, and **Elastic Net Regression**. Using the **Algerian Forest Fires Dataset** available on [Kaggle](https://www.kaggle.com/datasets/nitinchoudhary012/algerian-forest-fires-dataset), this project explores how these models can predict outcomes related to forest fires.

The user interface is built with **Streamlit** to provide a simple, interactive experience for selecting and comparing regression models.

## Features

- **Model Selection**: Choose from Linear Regression, Lasso Regression, Ridge Regression, and Elastic Net Regression.
- **Model Training**: Train selected models on the dataset and display metrics for comparison.
- **Prediction Visualization**: Plot predictions and evaluate the model’s performance.

## Getting Started

To get started with this project, follow these steps:

### Prerequisites

- Python 3.x
- pip package manager

### Installation
1. Clone the repository: 
    ```bash
    git clone https://github.com/nageCasillas/linear-regression.git
    cd linear-regression
    ```
2. Install the required packages:
   ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
4. Open your browser and go to http://localhost:8501 to start interacting with the app.

## Usage
1. Select a model type from the parameters.
2. Adjust parameters (if available) for the selected model.
3. Remember to fill every parameter.
4. View results and metrics for the trained model.

## Contribution
Contributions are welcome! If you would like to contribute, please:

1. Fork this repository.
2. Create a new branch (feature-branch-name).
3.Make changes and test them.
4. Create a pull request.

