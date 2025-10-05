import pandas as pd
import matplotlib.pyplot as plt

xmin, xmax = 5, 25
ymin, ymax = 2, 10

file_list = ['data1.csv', 'data2.csv', 'data3.csv', 'data5.csv', 'data6.csv', 't6.csv', 't7.csv', 't8.csv', 't9.csv', 't10.csv',
             't11.csv', 't12.csv']
bar_labels = ['Control 1', 'Control 2', 'Control 3', 'BM1', 'BM2', 'BM3', 'RR1', 'RR2', 'RR3', 'LT1', 'LT2', 'LT3']

files = []
center_percentages = []
out_of_center_percentages = []

for i, file_name in enumerate(file_list):
    try:
        file = pd.read_csv(file_name)
        file['In Center'] = (file['X (cm)'] >= xmin) & (file['X (cm)'] <= xmax) & (file['Y (cm)'] >= ymin) & (
                    file['Y (cm)'] <= ymax)
        center_count = file['In Center'].sum()
        out_of_center_count = len(file) - center_count

        center_percentage = (center_count / len(file)) * 100
        out_of_center_percentage = (out_of_center_count / len(file)) * 100

        files.append(bar_labels[i])
        center_percentages.append(center_percentage)
        out_of_center_percentages.append(out_of_center_percentage)

        print(f"{bar_labels[i]}: In Center: {center_percentage:.2f}%, Out of Center: {out_of_center_percentage:.2f}%")
    except FileNotFoundError:
        print(f"{file_name} not found. Skipping...")

plt.figure(figsize=(12, 6))
x = range(len(files))
plt.bar(x, center_percentages, color='green', label='In Center')
plt.bar(x, out_of_center_percentages, bottom=center_percentages, color='red', label='Out of Center')

plt.xticks(x, files, rotation=45)
plt.xlabel('Tests', fontsize=12)
plt.ylabel('Percentage', fontsize=12)
plt.title('Percentage Distribution', fontsize=14)
plt.legend()
plt.tight_layout()
plt.show()
