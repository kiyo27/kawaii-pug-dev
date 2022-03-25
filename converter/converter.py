import csv

input_file = 'edge.dt3'
output_file = 'output_edge.csv'

csv_file = open(input_file, 'r', encoding='utf-8')
f = csv.reader(csv_file, delimiter=':')

row = next(f)
x, y = row[0].split(',')
x = int(x)
y = int(y)

l = row[1].split(',')
L = list()
for i in range(y):
  tmp = list()
  for _ in range(x):
    tmp.append(l.pop(0))
  L.append(tmp)
print(L)

with open(output_file, 'w') as f:
  writer = csv.writer(f)
  for i, _ in enumerate(L):
    writer.writerow(L[i])

