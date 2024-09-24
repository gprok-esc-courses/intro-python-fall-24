import csv 

file = open("imdb.csv", encoding="utf-8")

reader = csv.DictReader(file)


for row in reader:
    try:
        score = int(row['Meta_score'])
        if score > 90:
            print(row['Series_Title'], row['Meta_score'])
    except ValueError:
        pass