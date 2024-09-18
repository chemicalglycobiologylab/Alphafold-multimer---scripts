# Alphafold-multimer---scripts

colabfold_analysis.py - adapted from Colabfold Batch AlphaFold-2-multimer structure analysis pipeline by Ernst Schmid "10.5281/zenodo.8223142"

This python script allows one to find contacts between residues in multimeric structure files produced as output from Alphafold2 via the Colabfold pipeline https://github.com/sokrypton/ColabFold/tree/main/colabfold. It integrates both physical proximity and Alphafold confidence metrics such as the predicted Alignment Error(pAE) and the predicted Local Distance Difference Test (pLDDT) to determine whether a pair of residues is a valid contact. It's external dependencies are numpy and pandas. Running this script will produce one or more folders each containing 3 comma seperated value (CSV) files that you can then open with a standard text editor or any spreadhseet program. The 3 files are: summary.csv, interfaces.csv, and contacts.csv. 

Jsonsort.py and plddtextract.py - inhouse scriupt to parse ipTm, pTm, and plddt scores from colab fold oputput Json files. 

plot confidence.py and Scatterplot_pTm+ipTm_VsPIDDT.py - inhiuse script for plot the data parse from Json into plot for identifying the beast models based on threshold "colors1 = ['gray' if (x >= 85 and y > 1.1) else 'lightgray' for x, y in zip(data1['pLDDT'], data1['ipTM+pTM'])]"

contactmaps.py - inhouse script for ploting 2D contact maps for Protein-protein complexes chain A and B, as mentioned in script. Usage: python3 contactmaps.py <pdb_file>"

contactmapsv2range.py- inhouse script for ploting 2D contact maps for Protein-protein complexes chain A and B along with marking the desired residues as range (for example active site 20-40 in chain A), as mentioned in script. python3 contactmapsv2range.py <pdb_file> <start_residue> <end_residue>"

contactmapsv1.py- inhouse script to plot 2D contact maps with labeling catalytic traid or any mumber residues of interest. Usage: python3 contactmapsv1.py example.pdb 5,10

