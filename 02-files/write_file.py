
# file = open("output.txt", "w")
file = open("output.txt", "a")

project = input("Project: ")
amount = input("Budget: ")

file.write(project + ": " + amount + "\n")

file.close()