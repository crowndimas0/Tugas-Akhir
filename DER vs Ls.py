import matplotlib.pyplot as plt
import numpy as np

x1 = df[['Ls']]
y1 = df[['Reff24', 'Reff25', 'Reff26', 'Reff27', 'Reff28', 'Reff29',
       'Reff30', 'Reff31', 'Reff32', 'Reff33', 'Reff34', 'Reff35']]

plt.figure(figsize=(12, 8))

plt.plot(x1, y1)
plt.plot(x1, y1['Reff24'], color='k')
plt.plot(x1, y1['Reff25'], color='royalblue', linestyle='--')
plt.plot(x1, y1['Reff26'], color='k')
plt.plot(x1, y1['Reff27'], color='k')
plt.plot(x1, y1['Reff28'], color='orange', linestyle='--')
plt.plot(x1, y1['Reff29'], color='k')
plt.plot(x1, y1['Reff30'], color='k')
plt.plot(x1, y1['Reff31'], color='k')
plt.plot(x1, y1['Reff32'], color='k')
plt.plot(x1, y1['Reff33'], color='k')
plt.plot(x1, y1['Reff34'], color='green', linestyle='--')
plt.plot(x1, y1['Reff35'], color='k')


plt.title('Kondisi $Dust$ $Effective$ $Radius$ pada Mars Years 24 - 35', weight='bold', loc='center', fontsize=18)
plt.xlabel('Bujur Matahari (°)', fontsize=16)
plt.ylabel('$Dust$ $Effective$ $Radius$ (m)', fontsize=16)
plt.xticks(np.arange(0, 370, 30))

# Show the legend
plt.legend(['MY25','MY28','MY34'],bbox_to_anchor=(0.12,1))

# Add vertical lines as separators
plt.axvline(x=89, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x=179, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x=269, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x=359, color='black', linestyle='--', linewidth=0.5)

plt.minorticks_on()
plt.grid(linestyle='--', linewidth=0.5)
plt.show()
