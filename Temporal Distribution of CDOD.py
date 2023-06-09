import pandas as pd
import matplotlib.pyplot as plt

# List nama file csv
files = {
    "dust_MY24.csv": "MY24",
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
    "dust_MY35.csv": "MY35"
}

# Create figure and subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Define color map and color range
cmap = plt.cm.get_cmap('jet')
num_files = len(files)

# Loop over files
for i, file in enumerate(files):
    # Load data into dataframe
    df = pd.read_csv('/content/drive/MyDrive/Dimas_Draft_Praproposal/Hasil/temporal analysis/' + file)

    # Group data by longitude and latitude, and compute mean cdod
    grouped_df = df.groupby('Ls').agg('cdod').mean().reset_index()

    # Create line plot with different colors and linestyles for each line
    color = cmap(i / num_files)  # Adjust the color based on the number of files

    linestyle = '-'  # Solid line by default
    if files[file] in ['MY25', 'MY28', 'MY34']:
        linestyle = '--'  # Dashed line for MY25, MY28, and MY34

    ax.plot(grouped_df['Ls'], grouped_df['cdod'], label=file, color=color, linestyle=linestyle)

# Set x and y labels and title
ax.set_xlabel('Bujur Matahari (°)', fontsize=16)
ax.set_ylabel('$Column$ $Dust$ $Optical$ $Depth$', fontsize=16)
ax.set_title('Kondisi Column Dust Optical Depth pada MY 24 - 35', weight='bold', ha='center')

# Add legend
ax.legend(['MY24', 'MY25', 'MY26', 'MY27', 'MY28',
           'MY29', 'MY30', 'MY31', 'MY32', 'MY33', 'MY34', 'MY35'], bbox_to_anchor=(0.15, 1))

# Add vertical lines as separators
ax.axvline(x=89, color='black', linestyle='--', linewidth=0.5)
ax.axvline(x=179, color='black', linestyle='--', linewidth=0.5)
ax.axvline(x=269, color='black', linestyle='--', linewidth=0.5)
ax.axvline(x=359, color='black', linestyle='--', linewidth=0.5)

# Display plot
plt.minorticks_on()
plt.grid(linestyle='--', linewidth=0.5)
plt.show()
