import csv

age = []
final = []
with open("titanic.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[3] == 'female':
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

with open("sex.csv", 'w') as k:
    writer = csv.writer(k)
    writer.writerow(final)