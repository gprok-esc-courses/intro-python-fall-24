import csv 

file = open("students.csv")

reader = csv.DictReader(file)

for row in reader:
    print(row['lastname'], row['gpa'])