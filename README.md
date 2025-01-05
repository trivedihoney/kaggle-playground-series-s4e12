# Kaggle Playground Series S4E12

This repository contains code and experiments for the Kaggle Playground Series Season 4 Episode 12 competition.

## Project Structure

- `insurance_premium_prediction.ipynb`: The main notebook containing the final model and analysis.
- `experiments/`: Directory containing various experimental notebooks.
    - `experiment_catboost.ipynb`: Experiments with CatBoost model.
    - `experiment_xgboost.ipynb`: Experiments with XGBoost model.
- `data/`: Directory containing the dataset files.
- `README.md`: Project documentation.
- `pyproject.toml`: Project dependencies and configuration.

## Setup

1. Clone the repository:
     ```bash
     git clone https://github.com/trivedhoney/kaggle-playground-series-s4e12.git
     cd kaggle-playground-series-s4e12
     ```

2. Install the required dependencies:
     ```bash
     uv sync
     ```

## Usage

1. Open `insurance_premium_prediction.ipynb` to see the final analysis and model training.

## Dependencies

- Python 3.12 or higher
- UV package manager
- CatBoost
- XGBoost
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Results

The final model achieved an RMSLE score of 1.04 on the test dataset.

## License

This project is licensed under the MIT License.