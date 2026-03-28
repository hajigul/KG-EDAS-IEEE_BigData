import numpy as np
import pandas as pd

class EDASCalculator:
    def __init__(self, X, models, criteria, non_beneficial, weights):
        self.X = X
        self.models = models
        self.criteria = criteria
        self.non_beneficial = non_beneficial
        self.weights = weights

    def compute_average_values(self):
        """Compute average for each criterion."""
        avg_values = np.mean(self.X, axis=0)
        avg_df = pd.DataFrame([avg_values], columns=self.criteria, index=['Average'])
        return avg_df, avg_values

    def compute_pda_nda(self, avg_values):
        """Compute Positive and Negative Distance matrices."""
        n_models, n_criteria = self.X.shape
        PDA = np.zeros((n_models, n_criteria))
        NDA = np.zeros((n_models, n_criteria))

        for j in range(n_criteria):
            avg_j = avg_values[j]
            is_nb = self.non_beneficial[j]
            for i in range(n_models):
                if not is_nb:  # beneficial
                    PDA[i, j] = max(0, self.X[i, j] - avg_j) / avg_j if avg_j != 0 else 0
                    NDA[i, j] = max(0, avg_j - self.X[i, j]) / avg_j if avg_j != 0 else 0
                else:  # non-beneficial
                    PDA[i, j] = max(0, avg_j - self.X[i, j]) / avg_j if avg_j != 0 else 0
                    NDA[i, j] = max(0, self.X[i, j] - avg_j) / avg_j if avg_j != 0 else 0

        PDA_df = pd.DataFrame(PDA, columns=self.criteria, index=self.models)
        NDA_df = pd.DataFrame(NDA, columns=self.criteria, index=self.models)
        return PDA_df, NDA_df

    def compute_weighted(self, PDA, NDA):
        """Apply weights to PDA and NDA."""
        WPDA = PDA * self.weights
        WNDA = NDA * self.weights
        WPDA_df = pd.DataFrame(WPDA, columns=self.criteria, index=self.models)
        WNDA_df = pd.DataFrame(WNDA, columns=self.criteria, index=self.models)
        return WPDA_df, WNDA_df

    def compute_scores(self, WPDA, WNDA):
        """Compute sums, normalize, and final M score."""
        WPDA_sum = np.sum(WPDA, axis=1)
        WNDA_sum = np.sum(WNDA, axis=1)

        max_WPDA = np.max(WPDA_sum) if np.max(WPDA_sum) != 0 else 1
        max_WNDA = np.max(WNDA_sum) if np.max(WNDA_sum) != 0 else 1

        NWPDA = WPDA_sum / max_WPDA
        NWNDA = WNDA_sum / max_WNDA

        M = 0.5 * (NWPDA + (1 - NWNDA))

        results_df = pd.DataFrame({
            'Model': self.models,
            'WPDA_sum': WPDA_sum,
            'WNDA_sum': WNDA_sum,
            'NWPDA': NWPDA,
            'NWNDA': NWNDA,
            'M': M
        })
        results_df = results_df.sort_values(by='M', ascending=False).reset_index(drop=True)
        return results_df

    def run(self):
        """Execute the full EDAS calculation."""
        avg_df, avg_values = self.compute_average_values()
        PDA_df, NDA_df = self.compute_pda_nda(avg_values)
        WPDA_df, WNDA_df = self.compute_weighted(PDA_df.values, NDA_df.values)
        results_df = self.compute_scores(WPDA_df.values, WNDA_df.values)
        return avg_df, PDA_df, NDA_df, WPDA_df, WNDA_df, results_df