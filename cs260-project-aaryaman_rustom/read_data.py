# src/read_data.py
import os
from kaggle.api.kaggle_api_extended import KaggleApi

def main():
    raw_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    os.makedirs(raw_dir, exist_ok=True)

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(
        'uciml/pima-indians-diabetes-database',
        path=raw_dir,
        unzip=True
    )
    print(f"Dataset downloaded and extracted to: {raw_dir}")

if __name__ == "__main__":
    main()
