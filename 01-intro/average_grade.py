total = 0
grade = 0

print("GRADE CALCULATOR")
for i in range(1, 4):
    grade = int(input("Give grade " + str(i) + ": "))
    total = total + grade

average = total / 3
print("Average: " + str(average))