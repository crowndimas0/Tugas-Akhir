import matplotlib.pyplot as plt
import numpy as np

x1 = df1[['Ls']]
y1 = df1[['Thermal24', 'Thermal25', 'Thermal26', 'Thermal27', 'Thermal28',
       'Thermal29', 'Thermal30', 'Thermal31', 'Thermal32', 'Thermal33',
       'Thermal34', 'Thermal35']]

plt.figure(figsize=(12, 8))

plt.plot(x1, y1)
plt.plot(x1, y1['Thermal24'], color='k')
plt.plot(x1, y1['Thermal25'], color='royalblue', linestyle='--')
plt.plot(x1, y1['Thermal26'], color='k')
plt.plot(x1, y1['Thermal27'], color='k')
plt.plot(x1, y1['Thermal28'], color='orange', linestyle='--')
plt.plot(x1, y1['Thermal29'], color='k')
plt.plot(x1, y1['Thermal30'], color='k')
plt.plot(x1, y1['Thermal31'], color='k')
plt.plot(x1, y1['Thermal32'], color='k')
plt.plot(x1, y1['Thermal33'], color='k')
plt.plot(x1, y1['Thermal34'], color='green', linestyle='--')
plt.plot(x1, y1['Thermal35'], color='k')

plt.title('Kondisi Thermal Infrared Flux to Space pada Mars Years 24 - 35', weight='bold', loc='center', fontsize=18)
plt.xlabel('Bujur Matahari (°)', fontsize=16)
plt.ylabel('$Thermal$ $Infrared$ $Flux$ $to$ $Space$ (W/m$^2$)', fontsize=16)
plt.xticks(np.arange(0, 370, 30))
plt.legend(['MY25','MY28','MY34'],bbox_to_anchor=(0.12,1))

# Add vertical lines as separators
plt.axvline(x=89, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x=179, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x=269, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x=359, color='black', linestyle='--', linewidth=0.5)

plt.minorticks_on()
plt.grid(linestyle='--', linewidth=0.5)
plt.show()
