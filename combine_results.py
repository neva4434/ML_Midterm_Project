
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parent

files = {
    "classifier_runs": 132,
    "classifier_summary": 44,
    "classifier_test": 2,
    "kmeans_runs": 12,
    "kmeans_summary": 4,
    "kmeans_test": 4,
}

for name, expected_rows in files.items():
    tables = []

    for dataset in ["breast_cancer", "wine"]:
        path = root / f"{dataset}_{name}.csv"

        if not path.exists():
            raise FileNotFoundError(f"Missing file: {path.name}")

        df = pd.read_csv(path, keep_default_na=False)
        tables.append(df)

    combined = pd.concat(tables, ignore_index=True)

    if len(combined) != expected_rows:
        raise ValueError(
            f"{name}: expected {expected_rows} rows, "
            f"found {len(combined)}"
        )

    output = root / f"{name}.csv"
    combined.to_csv(output, index=False)
    print(f"OK: {output.name} ({len(combined)} rows)")

print("\nAll six combined CSV files are ready.")
