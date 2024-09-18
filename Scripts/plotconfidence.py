import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV files into pandas DataFrames
df1 = pd.read_csv('uncaharacterizedMultimer_ptmiptm.csv')

# Define bins for the ranges
bins = [i for i in range(10, 110, 10)]

# Calculate the counts for each range for each DataFrame
counts1, _ = np.histogram(df1['Model_confidence%'], bins=bins)


# Define labels for each range
labels = [f'{bins[i]}-{bins[i+1]}' for i in range(len(bins)-1)]

# Plot individual bar chart for each DataFrame
plt.figure(figsize=(10, 6))
bar_width = 0.25
plt.bar(np.arange(len(labels)) - bar_width, counts1, width=bar_width, label='Plant cysteine protease + SUSS effectors', align='center', color='gray')

plt.xlabel('Model Confidence (%)')
plt.ylabel('Frequency')
plt.title('Model Confidence Distribution')
plt.xticks(np.arange(len(labels)), labels, rotation=45, ha='right')
plt.legend()

# Show plot
plt.tight_layout()
plt.show()

