total = 0
grade = 0

courses = ["Python", "Database", "Web", "Network", "Management", "US History"]

print("GRADE CALCULATOR")
for i in range(len(courses)):
    grade = int(input("Give grade " + courses[i] + ": "))
    total = total + grade

average = total / len(courses)
print("Average: " + str(average))