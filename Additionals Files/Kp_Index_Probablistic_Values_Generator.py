import csv
import random
import numpy as np

probabilities = [0.6427, 0.22, 0.089, 0.0323, 0.015, 0.001]
kp_ranges = [(0, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
data = []
for day in range(1, 501):
    kp_range = np.random.choice(len(probabilities), p=probabilities)
    kp_index = round(random.uniform(*kp_ranges[kp_range]), 2)
    estimated_kp = round(kp_index)
    data.append([day, kp_index, estimated_kp])

with open('kp_index_prediction_test1000.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["time_tag", "kp_index", "estimated_kp"])
    writer.writerows(data)

print("done")