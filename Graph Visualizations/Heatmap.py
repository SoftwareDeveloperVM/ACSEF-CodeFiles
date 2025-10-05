import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file = pd.read_csv('data3.csv')

cleaned_data = file[~((file['Y (cm)'] > 11.55) & ((file['X (cm)'] < 3.4) | (file['X (cm)'] > 28.7)))]

np.random.seed(42) 
scatter_strength_x = 0.6 
scatter_strength_y = 0.4  

cleaned_data['X (cm)'] += np.random.uniform(-scatter_strength_x, scatter_strength_x, size=len(cleaned_data))
cleaned_data['Y (cm)'] += np.random.uniform(-scatter_strength_y, scatter_strength_y, size=len(cleaned_data))
cleaned_data['X (cm)'] = -cleaned_data['X (cm)']
hm_data, xborder, yborder = np.histogram2d(cleaned_data['Y (cm)'], cleaned_data['X (cm)'], bins=(30, 30))
plt.figure(figsize=(12, 9))

colorbar_lowscale = np.percentile(hm_data, 1)
colorbar_highscale = np.percentile(hm_data, 99)

heatmap = sns.heatmap(hm_data.T, cmap='viridis', cbar_kws={'label': 'Fish Density'},
                      xticklabels=np.round(yborder, 1), yticklabels=np.round(xborder, 1),
                      vmin=colorbar_lowscale, vmax=colorbar_highscale,
                      square=True, linewidths=0.5, linecolor='gray')

plt.xlim(-28.7, -3.4) 
plt.ylim(0, 12) 

plt.xticks(ticks=np.arange(0, len(yborder), step=len(yborder) // 5), labels=np.round(yborder[::len(yborder) // 5], 1))
plt.yticks(ticks=np.arange(0, len(xborder), step=len(xborder) // 5), labels=np.round(xborder[::len(xborder) // 5], 1))
plt.xlabel('X (cm)', fontsize=14)
plt.ylabel('Y (cm)', fontsize=14)

plt.title('Fish Movement Heatmap (Reflected on Y-Axis)', fontsize=18, fontweight='bold')
plt.show()
