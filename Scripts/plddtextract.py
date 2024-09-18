from Bio.PDB import PDBParser
import os
import csv

def extract_column_from_pdb(pdb_file):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('structure', pdb_file)
    atoms = structure.get_atoms()
    column_values = []

    for atom in atoms:
        # Assuming column 10 corresponds to B-factor, change as needed
        column_values.append(atom.get_bfactor())

    # Calculate average
    average_value = sum(column_values) / len(column_values)
    return average_value

def main():
    pdb_directory = '/home/muthu/localcolabfold-1.5.5/outputdir/relaxed_PDB'
    output_csv_file = 'average_values.csv'

    with open(output_csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PDB_File', 'Average_Column_10_Value'])

        for pdb_file in os.listdir(pdb_directory):
            if pdb_file.endswith('.pdb'):
                pdb_path = os.path.join(pdb_directory, pdb_file)
                average_value = extract_column_from_pdb(pdb_path)
                writer.writerow([pdb_file, average_value])

    print("Average values saved to", output_csv_file)

if __name__ == "__main__":
    main()

