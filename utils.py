import numpy as np
import pandas as pd

def print_criteria_columns(criteria):
    """Print criteria columns with numbers."""
    print("\nDetected Criteria Columns:")
    for i, col in enumerate(criteria, 1):
        print(f"{i}. {col}")

def get_non_beneficial_indices(criteria):
    """Ask user to select non-beneficial criteria indices."""
    print("\n=== NON-BENEFICIAL CRITERIA SELECTION ===")
    print("Select which columns are non-beneficial (lower values are better, e.g., MR)")
    print("Enter column numbers separated by commas (e.g., 1,5,9) or leave blank if none:")
    selected = input("Your selection: ").strip()

    non_beneficial = [False] * len(criteria)
    if selected:
        try:
            selected_indices = [int(x.strip()) - 1 for x in selected.split(",")]
            for idx in selected_indices:
                if 0 <= idx < len(criteria):
                    non_beneficial[idx] = True
                else:
                    print(f"Warning: Index {idx+1} is out of range, ignoring")
        except ValueError:
            print("Invalid input. Using no non-beneficial criteria.")
    return np.array(non_beneficial)

def get_weights(criteria):
    """Ask user for weight assignment option and return weights array."""
    print("\n=== WEIGHT ASSIGNMENT OPTIONS ===")
    print("1. Assign equal weights to all criteria")
    print("2. Assign custom weights per metric type (same across all datasets)")
    weight_option = input("Select weight assignment option (1 or 2): ").strip()

    if weight_option == '1':
        n_criteria = len(criteria)
        weights = np.array([1.0 / n_criteria] * n_criteria)
        print(f"\nEqual weights assigned: {1/n_criteria:.4f} for each of {n_criteria} criteria")
        return weights

    # Custom weights: group by metric type
    print("\n=== CUSTOM WEIGHTS PER METRIC TYPE (APPLIED TO ALL DATASETS) ===")
    print("Your data has multiple datasets, each with: MR, MRR, H@1, H@10")
    print("You will assign weights to these 4 metric types.")
    print("Their sum must be exactly 1.0.\n")

    base_metrics = ['MR', 'MRR', 'H@1', 'H@10']
    metric_weights = {}
    remaining = 1.0
    for i, metric in enumerate(base_metrics):
        if i < len(base_metrics) - 1:
            while True:
                try:
                    prompt = f"Enter weight for '{metric}' (0 to {remaining:.2f}, {remaining:.2f} remaining): "
                    w = float(input(prompt))
                    if 0 <= w <= remaining + 1e-9:
                        metric_weights[metric] = w
                        remaining -= w
                        break
                    else:
                        print(f"Weight must be between 0 and {remaining:.4f}")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            metric_weights[metric] = remaining
            print(f"Automatically assigned remaining weight {remaining:.4f} to '{metric}'")

    print("\nAssigned metric-type weights (applied to all datasets):")
    for m, w in metric_weights.items():
        print(f"  {m}: {w:.4f}")
    print(f"  Total: {sum(metric_weights.values()):.4f}")

    # Map columns to weights
    weights_list = []
    for col in criteria:
        base_name = col.split('.')[0] if '.' in col else col
        if '@' in base_name:
            base_name = base_name.replace('@', '@')
        if base_name in metric_weights:
            weights_list.append(metric_weights[base_name])
        else:
            raise ValueError(f"Could not map column '{col}' to a base metric.")
    weights = np.array(weights_list)

    total_weight = np.sum(weights)
    if not np.isclose(total_weight, 1.0, atol=0.01):
        print(f"\nWarning: Total weight = {total_weight:.4f} (should be ~1.0)")
    else:
        print(f"\nTotal weight = {total_weight:.4f} ✓")

    return weights

def save_results(avg_df, PDA_df, NDA_df, WPDA_df, WNDA_df, results_df, output_dir):
    """Save all result DataFrames to CSV."""
    avg_df.to_csv(f"{output_dir}\\average_values.csv", index=False)
    PDA_df.to_csv(f"{output_dir}\\pda_values.csv", index=True)
    NDA_df.to_csv(f"{output_dir}\\nda_values.csv", index=True)
    WPDA_df.to_csv(f"{output_dir}\\wpda_values.csv", index=True)
    WNDA_df.to_csv(f"{output_dir}\\wnda_values.csv", index=True)
    results_df.to_csv(f"{output_dir}\\final_ranking.csv", index=False)

def display_results(avg_df, results_df):
    """Print summary of results."""
    print("\n=== AVERAGE VALUES ===")
    print(avg_df.round(4))
    print("\n=== FINAL RANKING (Top 10) ===")
    print(results_df[['Model', 'M', 'WPDA_sum', 'WNDA_sum']].head(10).round(4))