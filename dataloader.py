import pandas as pd

def load_data(file_path):
    """Load CSV file and return DataFrame."""
    return pd.read_csv(file_path)

def identify_model_column(data):
    """Identify the model column (usually 'Model' or first column)."""
    if 'Model' in data.columns:
        model_col = 'Model'
        criteria_cols = [col for col in data.columns if col != model_col]
    else:
        model_col = data.columns[0]
        criteria_cols = list(data.columns[1:])
    return model_col, criteria_cols

def extract_models_and_criteria(data, model_col, criteria_cols):
    """Extract models array and criteria matrix."""
    models = data[model_col].values
    X = data[criteria_cols].values
    return models, X, criteria_cols