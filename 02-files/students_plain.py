
file = open("students.csv")

lines = file.readlines()

for line in lines:
    line = str.strip(line)
    values = line.split(',')
    print(values[1], values[4])

