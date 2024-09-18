import os
import json
import csv

def extract_columns_from_json_folder(folder_path, output_file="merged_json.csv", columns=("ptm", "iptm")):
    with open(output_file, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["filename"] + list(columns))
        writer.writeheader()

        for filename in os.listdir(folder_path):
            if filename.endswith('.json'):
                with open(os.path.join(folder_path, filename), 'r') as file:
                    json_data = json.load(file)
                    extracted_data = {"filename": filename}
                    for column in columns:
                        if column in json_data:
                            extracted_data[column] = json_data[column]
                    writer.writerow(extracted_data)

# Example usage:
folder_path = "/home/muthu/localcolabfold-1.5.5/outputdir"
output_file = "fungi_ptmiptm.csv"
extract_columns_from_json_folder(folder_path, output_file)

