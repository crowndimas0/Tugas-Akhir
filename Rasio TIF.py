import matplotlib.pyplot as plt
import numpy as np

x1 = df1[['Ls']]
y1 = df1[[ 'kesetimbangan24', 'kesetimbangan25', 'kesetimbangan26',
       'kesetimbangan27', 'kesetimbangan28', 'kesetimbangan29',
       'kesetimbangan30', 'kesetimbangan31', 'kesetimbangan32',
       'kesetimbangan33', 'kesetimbangan34', 'kesetimbangan35']]
plt.figure(figsize=(12,8))
plt.plot(x1, y1)
plt.plot(x1, y1['kesetimbangan24'], color='k')
plt.plot(x1, y1['kesetimbangan25'], color='royalblue', linestyle='--')
plt.plot(x1, y1['kesetimbangan26'], color='k')
plt.plot(x1, y1['kesetimbangan27'], color='k')
plt.plot(x1, y1['kesetimbangan28'], color='orange', linestyle='--')
plt.plot(x1, y1['kesetimbangan29'], color='k')
plt.plot(x1, y1['kesetimbangan30'], color='k')
plt.plot(x1, y1['kesetimbangan31'], color='k')
plt.plot(x1, y1['kesetimbangan32'], color='k')
plt.plot(x1, y1['kesetimbangan33'], color='k')
plt.plot(x1, y1['kesetimbangan34'], color='green', linestyle='--')
plt.plot(x1, y1['kesetimbangan35'], color='k')
plt.title('Rasio $Thermal$ $Infrared$ $Flux$ $to$ $Space$ $and$ $on$ $Surface$ \npada Mars Years 24 - 35',weight='bold',loc='center',fontsize=18)
plt.xlabel('Bujur Matahari (°)', fontsize=16)
plt.ylabel('Rasio $Thermal$ $Infrared$ $Flux$ $to$ $Space$ $and$ $on$ $Surface$',fontsize=16)
plt.xticks(np.arange(0, 370, 30))
plt.legend(['MY25','MY28','MY34'],
           bbox_to_anchor=(0.13,0.15))

# Add vertical lines as separators
plt.axvline(x=89, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x=179, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x=269, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x=359, color='black', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.grid(linestyle='--', linewidth=0.5)
plt.show()
