import matplotlib.pyplot as plt
import numpy as np

def effectiveness_time(dosage, scale_factor):
    return scale_factor * np.log(dosage + 1) 

dosage_values = np.linspace(0.01, 10, 100)  # Dosage range from 0.01 mg to 10 mg for better curve visibility

effectiveness_L_theanine = effectiveness_time(dosage_values, scale_factor=12)  # L-theanine
effectiveness_Rhodiola = effectiveness_time(dosage_values, scale_factor=10)    # Rhodiola extract
effectiveness_Bacopa = effectiveness_time(dosage_values, scale_factor=8)      # Bacopa Monnieri

plt.figure(figsize=(10, 6))

plt.plot(dosage_values, effectiveness_L_theanine, label="L-theanine", color='blue')
plt.plot(dosage_values, effectiveness_Rhodiola, label="Rhodiola", color='green')
plt.plot(dosage_values, effectiveness_Bacopa, label="Bacopa", color='red')
plt.title('Effectiveness Time vs Dosage for Fish (Different Nootropics)')
plt.xlabel('Dosage (mg)')
plt.ylabel('Effectiveness Time (hours)')
plt.grid(True)
plt.legend()
plt.show()

# dosages for humans
# L-theanine 500 mg https://www.healthline.com/health/l-theanine
# Rhodiola extract 200-600 mg https://www.drugs.com/npp/rhodiola-rosea.html
# Bacopa Monnieri 300 mg https://www.drugs.com/npp/brahmi.html
