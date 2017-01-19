import csv

age = []
final = []
with open("titanic.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        v = row[4]
        if not v.strip():
            continue
        if '.' in v:
            v = float(v)
        v = int(v)
        age.append(v)
    print(age)
    for x in range(81):
        z = age.count(x)
        final.append({'x': x, 'y': z})
    print(final)

with open("project.csv", 'w') as k:
    writer = csv.writer(k)
    writer.writerow(final)