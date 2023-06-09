import pandas as pd
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

#lat_range_north = [x / 2 for x in range(80, 181)]
lat_range_south = [x / 2 for x in range(-80, -181, -1)]

for file in files:
    df = pd.read_csv('/content/drive/MyDrive/Dimas_Draft_Praproposal/Hasil/temporal analysis/' + file)
    #mean_cdod_north = df.loc[df['latitude'].isin(lat_range_north), 'cdod'].mean()
    mean_cdod_south = df.loc[df['latitude'].isin(lat_range_south), 'cdod'].mean()
    #print('Rata-rata CDOD pada {} di daerah Kutub Utara (60°N hingga 90°N): {:.3f}'.format(files[file], mean_cdod_north))
    print('Rata-rata CDOD pada {} di daerah Kutub Selatan (-60°S hingga -90°S): {:.3f}'.format(files[file], mean_cdod_south))
