import os
import json
import pandas as pd


# Dynamically resolve the root of the project
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")
CLEANED_DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned")


class FileHandler:
    """
    Handles all file operations for the AnimeRadar project.

    Responsibilities:
        - Loading individual raw JSON files from data/raw/
        - Combining all raw JSON files into a single dataset
        - Saving the combined dataset as a CSV for downstream processing
        - Providing utility functions for listing and validating raw files
    """

    def __init__(self, raw_path=RAW_DATA_PATH, cleaned_path=CLEANED_DATA_PATH):
        """
        Initialize FileHandler with paths to raw and cleaned data directories.

        Args:
            raw_path (str): Path to the folder containing raw JSON files.
            cleaned_path (str): Path to the folder where cleaned CSVs will be saved.
        """
        self.raw_path = raw_path
        self.cleaned_path = cleaned_path

        # Ensure the cleaned data directory exists
        os.makedirs(self.cleaned_path, exist_ok=True)


    def list_raw_files(self):
        """
        List all JSON files available in the raw data directory.

        Returns:
            list: Sorted list of JSON filenames (e.g., ['fall_2020.json', ...])
        """
        if not os.path.exists(self.raw_path):
            print(f"[Warning] Raw data folder not found: {self.raw_path}")
            return []

        files = [f for f in os.listdir(self.raw_path) if f.endswith(".json")]

        if not files:
            print("[Warning] No JSON files found in raw data folder.")
            return []

        return sorted(files)


    def load_single_file(self, filename):
        """
        Load a single raw JSON file and return its contents as a list of records.

        Args:
            filename (str): Name of the JSON file (e.g., 'fall_2020.json')

        Returns:
            list: List of anime records (dicts), or empty list if loading fails.
        """
        filepath = os.path.join(self.raw_path, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"  [Loaded] {filename} — {len(data)} records")
            return data

        except FileNotFoundError:
            print(f"  [Error] File not found: {filename}")
            return []

        except json.JSONDecodeError as e:
            print(f"  [Error] Failed to parse JSON in {filename}: {e}")
            return []


    def combine_all_files(self):
        """
        Load and combine all raw JSON files into a single pandas DataFrame.

        Iterates through every JSON file in the raw data folder, loads each one,
        and concatenates them into one unified dataset ready for preprocessing.

        Returns:
            pd.DataFrame: Combined dataset of all seasonal anime records.
                          Returns an empty DataFrame if no files are found.
        """
        raw_files = self.list_raw_files()

        if not raw_files:
            print("[Error] No files to combine. Returning empty DataFrame.")
            return pd.DataFrame()

        all_records = []

        print(f"\nLoading {len(raw_files)} raw JSON files...\n")

        for filename in raw_files:
            records = self.load_single_file(filename)
            all_records.extend(records)

        if not all_records:
            print("[Error] All files were empty or failed to load.")
            return pd.DataFrame()

        # Combine into a single DataFrame
        combined_df = pd.DataFrame(all_records)

        print(f"\n[Done] Combined dataset: {len(combined_df)} total records "
              f"from {len(raw_files)} files.\n")

        return combined_df


    def save_combined_csv(self, df, filename="combined_raw.csv"):
        """
        Save the combined DataFrame as a CSV file in the cleaned data directory.

        This CSV serves as the input for Ree's preprocessing/cleaning stage.

        Args:
            df (pd.DataFrame): The combined anime dataset to save.
            filename (str): Output filename. Defaults to 'combined_raw.csv'.

        Returns:
            str: Full path to the saved CSV file.
        """
        if df.empty:
            print("[Warning] DataFrame is empty. Nothing saved.")
            return None

        output_path = os.path.join(self.cleaned_path, filename)
        df.to_csv(output_path, index=False, encoding="utf-8")

        print(f"[Saved] Combined CSV saved to: {output_path}")
        print(f"        Shape: {df.shape[0]} rows x {df.shape[1]} columns")

        return output_path


    def load_cleaned_csv(self, filename="cleaned_data.csv"):
        """
        Load a cleaned CSV file from the cleaned data directory.

        Used by downstream modules (ranking, statistics, visualization)
        to load Ree's preprocessed output.

        Args:
            filename (str): Name of the cleaned CSV file to load.

        Returns:
            pd.DataFrame: Loaded DataFrame, or empty DataFrame if file not found.
        """
        filepath = os.path.join(self.cleaned_path, filename)

        try:
            df = pd.read_csv(filepath, encoding="utf-8")
            print(f"[Loaded] Cleaned CSV: {filename} — "
                  f"{df.shape[0]} rows x {df.shape[1]} columns")
            return df

        except FileNotFoundError:
            print(f"[Error] Cleaned file not found: {filepath}")
            return pd.DataFrame()

        except Exception as e:
            print(f"[Error] Failed to load cleaned CSV: {e}")
            return pd.DataFrame()


    def get_summary(self, df):
        """
        Print a quick summary of the combined dataset.

        Useful for verifying the data before passing it to preprocessing.

        Args:
            df (pd.DataFrame): The combined dataset.
        """
        if df.empty:
            print("[Summary] DataFrame is empty.")
            return

        print("\n========== Dataset Summary ==========")
        print(f"Total records      : {len(df)}")
        print(f"Columns            : {list(df.columns)}")
        print(f"Seasons covered    : {sorted(df['season'].unique()) if 'season' in df.columns else 'N/A'}")
        print(f"Years covered      : {sorted(df['year'].unique()) if 'year' in df.columns else 'N/A'}")
        print(f"Missing values     :\n{df.isnull().sum()}")
        print("=====================================\n")


# ── Main: Run this file directly to test the FileHandler ──────────────────────
if __name__ == "__main__":

    handler = FileHandler()

    # Step 1: List all available raw files
    print("=== Available Raw Files ===")
    files = handler.list_raw_files()
    for f in files:
        print(f"  - {f}")

    # Step 2: Combine all raw JSON files into one DataFrame
    print("\n=== Combining All Files ===")
    combined_df = handler.combine_all_files()

    # Step 3: Print a summary of the combined data
    handler.get_summary(combined_df)

    # Step 4: Save as CSV for Ree's preprocessing stage
    print("=== Saving Combined CSV ===")
    handler.save_combined_csv(combined_df, filename="combined_raw.csv")