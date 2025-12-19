# a = 10
# print(a/0)   # ZeroDivisionError

# b = int('abc')
# print(b)      # ValueError

# a = 10
# b = 'a'
# c = a+b
# print(c)        #TypeEror

# list = [1,2,3]
# print(list[4])     # Index Error

# dict = {
#     'name' : 'dip',
#     'age' : 19
# }
# print(dict['city'])     #KeyError

with open("names.txt","r") as f:
    data = f.read()                 #fileNotFound