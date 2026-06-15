# Goal of this script is to load CSVs, check the columns, count rows
# and export a JSONL

import csv
import json
import os

csv_file_path = "../data/raw/dataset_c.csv"
jsonl_file_path = "../data/processed/dataset_c.jsonl"

os.makedirs("../data/processed", exist_ok=True)

def read_csv_with_fallback(path):
    encodings = ["utf-8-sig", "utf-8", "cp1252", "latin-1"]

    for encoding in encodings:
        try:
            with open(path, mode="r", encoding=encoding, newline="") as csv_file:
                rows = list(csv.DictReader(csv_file))
                print(f"Successfully read {path} using {encoding}")
                return rows
        except UnicodeDecodeError:
            print(f"Failed with {encoding}")

    raise ValueError("Could not read CSV with common encodings.")

data = read_csv_with_fallback(csv_file_path)

with open(jsonl_file_path, mode="w", encoding="utf-8") as jsonl_file:
    for row in data:
        jsonl_file.write(json.dumps(row, ensure_ascii=False) + "\n")

print(f"Saved JSONL to {jsonl_file_path}")