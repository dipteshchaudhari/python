import csv

# with open("scores.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# with open("scores.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

# Write Csv File

# data = [
#     ["name","age","city"],
#     ["dip",19,"aehmedabad"],
#     ["Raj",20,"Surat"]
# ]

# with open("output.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# Write dictionary-based CSV

# import csv

# students = [
#     {"name" : "Dip","age" : 19,"city":"Aehmedabad"},
#     {"name" : "Smit","age" : 19,"city" : "Surat"}
# ]   
# with open("students.csv","w",newline="") as file:

#     fieldnames = ["name","age","city"]
#     writer = csv.DictWriter(file,fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerows(students)

# JSON = JavaScript Object Notation

# import json

# with open("data.json","r") as file:
#     data = json.load(file)
# print(data)
# print(data["name"])

# # writng json file

# import json

# student = {
#     "name" : "Diptesh",
#     "Age" : 19,
#     "skills" : ["python","java"]
# }

# with open("student.json","w") as file:

#     json.dump(student,file,indent=4)