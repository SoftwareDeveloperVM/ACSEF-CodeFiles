import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('t6.csv')
x_min = df['X (cm)'].min()
x_max = df['X (cm)'].max()
y_min = df['Y (cm)'].min()
y_max = df['Y (cm)'].max()

center_x_min = (x_max + x_min) / 2 - (x_max - x_min) * 0.25
center_x_max = (x_max + x_min) / 2 + (x_max - x_min) * 0.25 
center_y_min = (y_max + y_min) / 2 - (y_max - y_min) * 0.25 
center_y_max = (y_max + y_min) / 2 + (y_max - y_min) * 0.25  
df['In Center'] = (df['X (cm)'] >= center_x_min) & (df['X (cm)'] <= center_x_max) & (df['Y (cm)'] >= center_y_min) & (df['Y (cm)'] <= center_y_max)

plt.figure(figsize=(10, 8))

plt.scatter(df[df['In Center']]['X (cm)'], df[df['In Center']]['Y (cm)'], color='green', label='In Center')

plt.scatter(df[~df['In Center']]['X (cm)'], df[~df['In Center']]['Y (cm)'], color='red', label='Out of Center')

plt.xlabel('X (cm)', fontsize=14)
plt.ylabel('Y (cm)', fontsize=14)
plt.title('Scatter Plot', fontsize=16)
plt.legend()
plt.show()
