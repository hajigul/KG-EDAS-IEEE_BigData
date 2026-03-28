import os
from dataloader import load_data, identify_model_column, extract_models_and_criteria
from utils import (print_criteria_columns, get_non_beneficial_indices,
                   get_weights, save_results, display_results)
from edas import EDASCalculator

def main():
    # Configuration
    file_path = r"D:\EDAS\tail_new\tail_prediction_results.csv"  # Update if needed
    output_dir = r"D:\EDAS\tail_new"

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Load data
    data = load_data(file_path)
    model_col, criteria_cols = identify_model_column(data)
    models, X, criteria = extract_models_and_criteria(data, model_col, criteria_cols)

    # User input: print criteria columns
    print_criteria_columns(criteria)

    # User input: non-beneficial criteria
    non_beneficial = get_non_beneficial_indices(criteria)

    # User input: weights
    weights = get_weights(criteria)

    # Perform EDAS calculation
    calculator = EDASCalculator(X, models, criteria, non_beneficial, weights)
    avg_df, PDA_df, NDA_df, WPDA_df, WNDA_df, results_df = calculator.run()

    # Save results
    save_results(avg_df, PDA_df, NDA_df, WPDA_df, WNDA_df, results_df, output_dir)

    # Display summary
    display_results(avg_df, results_df)
    print("\nFull results saved to:", output_dir)

if __name__ == "__main__":
    main()