import pandas as pd
from pandas.api.types import is_numeric_dtype
import stats_funcs as stats
import math
import sys


def clean_values(values):
    return [
        v
        for v in values
        if v is not None and not (isinstance(v, float) and math.isnan(v))
    ]


def describe(df):
    stats_map = [
        ("count", lambda s: stats.count(s)),
        ("mean", lambda s: stats.mean(s)),
        ("std", lambda s: stats.std(s)),
        ("min", lambda s: stats.minimum(s)),
        ("25%", lambda s: stats.quantile(s, 0.25)),
        ("50%", lambda s: stats.median(s)),
        ("75%", lambda s: stats.quantile(s, 0.75)),
        ("max", lambda s: stats.maximum(s)),
    ]

    numeric_cols = [col for col in df.columns if is_numeric_dtype(df[col])]

    data = {}
    for col in numeric_cols:
        cleaned = clean_values(df[col])
        data[col] = [func(cleaned) for _, func in stats_map]

    return pd.DataFrame(data, index=[label for label, _ in stats_map])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        df = pd.read_csv(file_name)
    else:
        print("Please provide a CSV file name as a command line argument.")
        sys.exit(1)
    print(describe(df))
