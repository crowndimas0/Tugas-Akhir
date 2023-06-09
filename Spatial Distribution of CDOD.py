import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# List nama file csv
files = {"dust_MY24.csv": "MY24", 
         "dust_MY25.csv": "MY25", 
         "dust_MY26.csv": "MY26", 
         "dust_MY27.csv": "MY27", 
         "dust_MY28.csv": "MY28", 
         "dust_MY29.csv": "MY29", 
         "dust_MY30.csv": "MY30", 
         "dust_MY31.csv": "MY31", 
         "dust_MY32.csv": "MY32",
         "dust_MY33.csv": "MY33",
         "dust_MY34.csv": "MY34",
         "dust_MY35.csv": "MY35"}
# Create figure with subplots
fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(18, 18))

# Define color map and color range
cmap = 'jet'
vmin = 0.01
vmax = 0.4

# Loop over files
for i, file in enumerate(files):
    # Load data into dataframe
    df = pd.read_csv('/content/drive/MyDrive/Dimas_Draft_Praproposal/Hasil/temporal analysis/' + file)

    # Group data by longitude and latitude, and compute mean cdod
    grouped_df = df.groupby(['longitude', 'latitude']).agg('cdod').mean().reset_index()

    # Select subplot based on row and column index
    row = i // 3
    col = i % 3
    ax = axes[row, col]

    # Create scatter plot with fixed color map and color range
    sc = ax.scatter(grouped_df['longitude'], grouped_df['latitude'], c=grouped_df['cdod'], cmap=cmap, vmin=vmin, vmax=vmax)
    ax.set_xlabel('Longitude', fontsize = 16)
    ax.set_ylabel('Latitude', fontsize = 16)
    ax.set_xticks([-180,0,180])
    ax.set_yticks([-45,0,45])
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.set_title('{}'.format(files[file]))

# Adjust subplot spacing and display plot
cax = fig.add_axes([0.9, 0.2, 0.02, 0.6])  
cbar = fig.colorbar(sc, cax=cax, orientation='vertical')
cbar.ax.tick_params(labelsize=16)
fig.suptitle('Kondisi Column Dust Optical Depth pada MY24 - M35\n ', weight='bold', ha='center', fontsize = 16)
fig.subplots_adjust(right=0.88, wspace=0.25, top=0.95, hspace=0.3)   
plt.show()
