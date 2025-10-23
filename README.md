# Diabetes Prediction Using Decision Tree Models

This project applies machine learning to the well-known diabetes dataset for binary classification (outcome prediction). It demonstrates how various train-test splits and random seeds affect the model's accuracy. The model used is primarily a Decision Tree (with both regression and classifier approaches), and the best accuracy scores for each configuration are logged for analysis.

## Features

- Uses the **diabetes.csv** dataset
- Splits data using different test sizes and random seeds for robustness
- Trains and evaluates a DecisionTreeRegressor and DecisionTreeClassifier from `scikit-learn`
- Logs the highest accuracy scores into **text2.csv**
- Utilizes classic ML libraries and Python tools like pandas, numpy, scikit-learn, and csv

## Installation

1. Clone the repository:


2. **Install dependencies:**

3. **Add the diabetes dataset named `diabetes.csv` to the project folder.**

## Usage

1. **Run the script:**

2. The script will:
- Load and preprocess data
- Train multiple Decision Tree models with different splits and seeds
- Print results and save best scores to `text2.csv`

## Output

- Accuracy scores and model predictions printed to console
- Best accuracy for each config appended to `text2.csv` for review

## Project Structure

- `main.py` - Main ML code
- `diabetes.csv` - Input dataset file (user-supplied)
- `text2.csv` - Output file, stores best results

## License

MIT License

## Author

Druhin Mitra
