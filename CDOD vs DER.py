import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# List MY numbers
MY_numbers = ['MY24', 'MY25', 'MY26', 'MY27', 'MY28', 'MY29', 'MY30', 'MY31', 'MY32', 'MY33', 'MY34', 'MY35']

# Read the CSV file
df = pd.read_csv('/content/cdod dan der - cdodvsder.csv')

# Create a figure with subplots
fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(18, 18))

# Loop over MY numbers
for i, MY in enumerate(MY_numbers):
    # Select subplot based on row and column index
    row = i // 3
    col = i % 3
    ax = axes[row, col]

    # Filter data for the specific MY
    MY_column = 'cdod' + MY[-2:]
    Reff_column = 'Reff' + MY[-2:]
    filtered_df = df[[MY_column, Reff_column]]

    # Create scatter plot with log-scaled Reff
    if MY in ['MY25', 'MY28', 'MY34']:
        # Highlight specific MY with different marker color and size
        ax.scatter(y=filtered_df[MY_column], x=np.log10(filtered_df[Reff_column]), alpha=0.5, color='red', marker='o', s=50)
    else:
        ax.scatter(y=filtered_df[MY_column], x=np.log10(filtered_df[Reff_column]), alpha=0.5)

    # Set labels and title
    ax.set_xlabel('$Dust$ $Effective$ $Radius$ (m)', fontsize = 16)
    ax.set_ylabel('$Column$ $Dust$ $Optical$ $Depth$', fontsize = 16)
    ax.set_title('{}'.format(MY))

# Adjust subplot spacing and display plot
fig.suptitle('Hubungan Column Dust Optical Depth terhadap Dust Effective Radius\n', weight='bold', fontsize=16)
fig.tight_layout()
plt.show()
