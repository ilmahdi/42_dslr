import pandas as pd
import sys


def describe(df):
    for col in df.dtypes.index:
        if df[col].dtype == 'float64':
            print(f"Column: {col}")
            return

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        df = pd.read_csv(file_name)
    else:
        print("Please provide a CSV file name as a command line argument.")
        sys.exit(1)
    print(describe(df))