import numpy as np
import pandas as pd
import zipfile

class WineQuality:  # or WineQuality()
    def __init__(self):
        # Add all variables specific to the class here
        self.df = None
        self.train_df = None
        self.test_df = None

    def read(self, path: str):
        """Read in and clean data"""
        zf = zipfile.ZipFile(path)
        self.df = pd.read_csv(zf.open('winequality-white.csv'), sep=';')

    def train(self, test_frac: float = 0.1):
        """Return ONLY the training data. Identify the training data
        if it does not yet exist."""
        if self.train_df is None:
            self._train_test_split(test_frac)
        return self.train_df

    def test(self, test_frac: float = 0.1):
        """Return ONLY the training data. Identify the training data
        if it does not yet exist."""
        if self.test_df is None:
            self._train_test_split(test_frac)
        return self.test_df

   # If it starts with an underscore, you're officially not allowed to
   # reference it from another file 
    def _train_test_split(self, test_frac: float):
        """Randomly train test split the dataframe."""
        all_rows = np.arange(len(self.df))
        np.random.shuffle(all_rows)
        test_n_rows = round(len(self.df)*test_frac)
        test_rows = all_rows[:test_n_rows]
        train_rows = all_rows[test_n_rows:]

        self.train_df = self.df.loc[train_rows].reset_index(drop=True)
        self.test_df = self.df.loc[test_rows].reset_index(drop=True)


if __name__ == '__main__':
    wq = WineQuality()
    wq.read('data/wine_quality.zip')
    print(wq.test())