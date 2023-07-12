import json
import csv
import os
from typing import List, Dict
from flatten_json import flatten

def find_lists_of_dicts(obj):
    """
    Find all lists of dictionaries in a JSON-like object.
    Returns a list of lists of dictionaries.
    """
    results = []
    if isinstance(obj, list) and all(isinstance(i, dict) for i in obj):
        results.append(obj)
    if isinstance(obj, dict):
        for k, v in obj.items():
            results.extend(find_lists_of_dicts(v))
    return results

def load_json_file(json_file_path: str) -> List[List[Dict]]:
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        return find_lists_of_dicts(data)
    except FileNotFoundError:
        print(f"The file {json_file_path} does not exist.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {json_file_path}.")
        return []

def write_to_csv(data: List[Dict], csv_file_path: str):
    if data:
        # Flattening the JSON and getting the keys for CSV header
        flat_data = [flatten(d) for d in data]
        csv_columns = list(flat_data[0].keys())

        try:
            with open(csv_file_path, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for row in flat_data:
                    writer.writerow(row)
            print(f"Data has been written to {csv_file_path}")
        except IOError:
            print(f"I/O error while writing to CSV file {csv_file_path}.")
    else:
        print("Empty data. The CSV file was not created.")

if __name__ == "__main__":
    json_file_path = input("Enter the path to your JSON file: ").strip()
    csv_file_path_template = input("Enter the template for your output CSV files' path (use {i} for the index of the list): ").strip()

    lists_of_dicts = load_json_file(json_file_path)
    for i, data in enumerate(lists_of_dicts):
        write_to_csv(data, csv_file_path_template.format(i=i))
