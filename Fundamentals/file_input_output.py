# f = open("file.txt","r")
# data = f.read()
# print(data)
# f.close() 

# f = open("file.txt","w")
# f.write("using write function!!\n")   #<--overwrite if file already exists
# f.write("smit\n")
# f.write("himang\n")
# f.close()

# reading file line by line
# f = open("file.txt","r")
# for line in f:
#     print(line.strip())
# f.close()

# Use .strip() to remove unwanted spaces or newline characters (\n).

# read one line 
# f = open("file.txt","r")
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# f.close()

# Read All Lines into List
# f = open("file.txt","r")
# data = f.readlines()
# print(data)
# f.close()


# with statement
# with open("file.txt","w") as f:
#     f.write("lata mangeshkar")

# with open("file.txt","a") as f:
#     f.write("\nAR rehman")

# if file not exist when we write data to it ,python will create a file of it

# with open("practice.txt","w") as f :
#     f.write("creating a file")

# r+ mode

# with open("file.txt","r+") as f:

#     f.write("\nkanha chaudhary")
    
#     data = f.read()
#     print(data)         #<-- pointer is at y so when we read file it will read after y character in this file

# w+ mode

# with open("file.txt","w+") as f :
#     print(f.read())
#     f.write("this is diptesh!!")
#     f.write("\nfile input output")

# with open("file.txt","a+") as f:
#     f.write("\nusing a+")
#     print(f.read())


# deleting a file:

# using os module
# import os 
# os.remove("sample.txt")

# practice : create a file with this data 
# with open("prac.txt","w") as f:
#     f.write("Hi Everyone\n")
#     f.write("i am learning file I/o\n")
#     f.write("using java\n")
#     f.write("and i love java")

# creating a function that replace java with python 

# first we read the data 
# with open("prac.txt","r") as f:
#         data = f.read()

# # then with that data we performed replace operation for replacing python with java
# new_Data = data.replace("java", "python")
# print(new_Data)

# #then we simply overwrite that file with new data 
# with open("prac.txt","w") as f:
#         f.write(new_Data)


#search the word learning exists in the data or not



              
# making function for this :
# def search_word():
#     word = "learning"
#     with open("prac.txt","r") as f:
#         data = f.read()

#         if(data.find(word) != -1):
#             print("Found that word")
#         else:
#             print("Not Found") 
 
# search_word()


# write a function to find in which line of the file the "learning" word occur first

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("prac.txt","r") as f:
#         while data:
#             data = f.readline()
#             if (word in data) :
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# check_for_line()



# json module


# import json

# data = {"name" : "dip" , "age" : 19}

# with open("data.json","w") as f:
#     json.dump(data,f,indent=4)

# with open("data.json","r") as f:
#     data = json.load(f)
# print(data)


# csv file handling

# import csv

# with open("names.csv","r") as f:
#     reader = csv.reader(f)

#     for line in reader:
#         print(line)


