# Divide data to 10 files
import pandas
import math
import data_tokenization as dt
import numpy as np
# Load dataset
filename = 'kickstarter_scaled.csv'
array = dt.load_csv(filename)
# array = str(array)
# with open('inny.txt', 'w') as f:
#     f.write(array)
# print(array)
successful = []
failed = []

for row in array:
    failed.append(row) if int(float(row[8])) == 0 else successful.append(row)

print(len(failed))
print(len(successful))
successful_in_subset = math.floor(len(successful) / 10)
failed_in_subset = math.floor(len(failed) / 10)
print(successful_in_subset)
print(failed_in_subset)
for i in range(1, 10):
    subset = []
    for s in range(0, successful_in_subset-1):
        subset.append(successful.pop())
    for f in range(0, failed_in_subset-1):
        subset.append(failed.pop())

    f = open('%d.csv' % i, 'w')
    f.write("\n".join([";".join(i) for i in subset]))
    print('done')
    f.close()

subset = successful + failed
f = open('10.csv', 'w')
f.write("\n".join([";".join(i) for i in subset]))

print('done')
f.close()
