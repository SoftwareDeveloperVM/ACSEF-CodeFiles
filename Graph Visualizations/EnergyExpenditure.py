import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 't12.csv'

fish_mass = 0.0005
data = pd.read_csv(file)
data['Speed_m_s'] = data['Speed (cm/s)'] / 100
data['Kinetic_Energy_J'] = 0.5 * fish_mass * (data['Speed_m_s']**2)
time_interval = np.diff(data['Time (s)'])


total_energy = np.sum(data['Kinetic_Energy_J'].iloc[1:] * time_interval)
print(f"Total Energy Expenditure for {file}: {total_energy:.4f} Joules")
plt.figure(figsize=(12, 8))
plt.plot(data['Time (s)'], data['Kinetic_Energy_J'], label=f'{file} Kinetic Energy')

plt.xlabel('Time (s)')
plt.ylabel('Kinetic Energy (J)')
plt.title('Kinetic Energy Over Time')
plt.legend()
plt.grid(True)
plt.show()
