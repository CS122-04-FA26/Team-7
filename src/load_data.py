from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "netflix_titles.csv"


def load_netflix_data():
    """Load the Netflix dataset from the data folder."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH}. See data/README.md for download steps."
        )
    return pd.read_csv(DATA_PATH)


if __name__ == "__main__":
    df = load_netflix_data()
    print(df.shape)
    print(df.head())