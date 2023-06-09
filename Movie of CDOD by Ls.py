import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Load data into dataframe
df = pd.read_csv('/content/drive/MyDrive/Dimas_Draft_Praproposal/Hasil/temporal analysis/dust_MY25.csv')

cmap = 'jet'
vmin = 0
vmax = 2

for i, Ls in enumerate(df['Ls'].unique()):
  df_ls = df[df['Ls'] == Ls]

  fig, ax = plt.subplots(figsize=(8, 6))
  sc = ax.scatter(df_ls['longitude'], df_ls['latitude'], c=df_ls['cdod'], cmap=cmap, vmin=vmin, vmax=vmax)
  ax.set_xlabel('Longitude', fontsize=12)
  ax.set_ylabel('Latitude', fontsize=12)
  ax.set_xticks([-180, 0, 180])
  ax.set_yticks([-45, 0, 45])
  ax.tick_params(axis='both', which='major', labelsize=8)
  ax.set_title('Ls = {}'.format(Ls), fontsize=10)
  plt.savefig("MY25_cdod_Ls_"+str(i)+".png", dpi=150)
  plt.close()

import moviepy.video.io.ImageSequenceClip

images = []
for i in range(669):
  filename = "MY25_cdod_Ls_"+str(i)+".png"
  images.append(filename)

fps = 60

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(images, fps=fps)
clip.write_videofile('MY25.mp4')
