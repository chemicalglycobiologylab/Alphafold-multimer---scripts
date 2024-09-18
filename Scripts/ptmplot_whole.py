import pandas as pd
import matplotlib.pyplot as plt

# Read the first CSV file
data1 = pd.read_csv('uncaharacterizedMultimer_ptmiptm.csv')


# Combine all datasets
combined_data = pd.concat([data1], ignore_index=True)

# Extract the columns for all datasets
x_values1 = data1['pLDDT']
y_values1 = data1['ipTM+pTM']

# Define colors based on conditions for all datasets
colors1 = ['gray' if (x >= 85 and y > 1.1) else 'lightgray' for x, y in zip(data1['pLDDT'], data1['ipTM+pTM'])]


# Plot the scatter plot for all datasets
plt.figure(figsize=(10, 6))
plt.scatter(x_values1, y_values1, color=colors1, alpha=0.5, label='Plant cysteine protease + SUSS effectors')

# Add cutoff lines
plt.axvline(x=85, color='red', linestyle='--', label='pLDDT Cutoff')
plt.axhline(y=1.1, color='red', linestyle='--', label='ipTM+pTM Cutoff')

# Add labels and legend
plt.xlabel('pLDDT')
plt.ylabel('ipTM+pTM')
plt.legend()
plt.show()

