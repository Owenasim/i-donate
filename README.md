# Cartesi Linear Regression DApp

## Overview

This is a decentralized application (DApp) built on the Cartesi platform that implements linear regression functionality. It allows users to manage datasets, train linear regression models, make predictions, and evaluate model performance. The DApp leverages Cartesi's computational capabilities to perform machine learning tasks in a decentralized environment.

## Features

- **Data Management**: Add and clear datasets for model training and evaluation.
- **Model Training**: Train linear regression models on the stored dataset.
- **Predictions**: Make predictions using the trained model.
- **Model Evaluation**: Compute and retrieve model performance metrics.
- **Model Persistence**: Save and load model parameters.
- **Inspection Endpoints**: Retrieve model details, predictions, and data summaries.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/cartesi-linear-regression.git
   cd cartesi-linear-regression
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the DApp**:
   ```bash
   python main.py
   ```

## API Endpoints

### Advance Commands

- **ADD_DATA**: Adds new data points to the dataset.
- **TRAIN_MODEL**: Trains the linear regression model on the current dataset.
- **PREDICT**: Makes predictions using the trained model.
- **SAVE_MODEL**: Saves the current model parameters.
- **LOAD_MODEL**: Loads model parameters.
- **CLEAR_DATA**: Clears all stored data.

### Inspection Endpoints

- **/predict**: Make predictions using the current model and dataset.
- **/model_params**: Retrieve the current model parameters.
- **/model_metrics**: Get the latest model performance metrics.
- **/data_summary**: Get a summary of the current dataset.

## Example Usage

- **Adding Data**:

  ```json
  {
    "command": "ADD_DATA",
    "data": {
      "X": [
        [1, 2],
        [2, 3],
        [3, 4]
      ],
      "y": [2, 3, 4]
    }
  }
  ```

- **Training the Model**:

  ```json
  {
    "command": "TRAIN_MODEL"
  }
  ```

- **Making Predictions**:

  ```json
  {
    "command": "PREDICT",
    "data": {
      "X": [
        [4, 5],
        [5, 6]
      ]
    }
  }
  ```

- **Saving the Model**:
  ```json
  {
    "command": "SAVE_MODEL"
  }
  ```

## Machine Learning Details

The DApp uses scikit-learn's LinearRegression model for implementing linear regression. It includes functionality for:

- Splitting data into training and testing sets
- Computing Mean Squared Error (MSE) and R-squared metrics
- Handling model coefficients and intercept

## Contributing

Contributions to improve the DApp are welcome. Please feel free to submit issues and pull requests.
