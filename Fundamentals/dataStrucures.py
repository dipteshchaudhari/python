# lists : ordered , mutable and dynamically sequenced --> indexing preserved, modify its 
# element and their size can grow or shrinks

lst = [10, "alex" , True , 3.234]
# indexing
print(lst[3])
# adding elemtns 
lst.append(50) 
print(lst) 
lst.insert(2,"alia") 
print(lst) 

# removing elements
lst.remove("alex")  #<--remove this perticular element 
print(lst)

lst.pop()   #<-- last element pop
print(lst)

lst.pop(2)  #<--pop element with index  
print(lst)

# updating items
lst[2] = 3.14
print(lst)

# sort()
l = [1,2,3,6,5,4]
l.sort()                
l.sort(reverse=True)
print(l)

words = ['banana','apple','kaaju']
words.sort()
print(words)

# reverseing a list
l.reverse()

# clear whole list
items = [1,23.4,'kaju','katali']
items.clear()
print(items)    #<-- empty list

# count : how many time a value appears in a list 
list = [1,2,3,12,3,5,6,4,2,4,3,3]
ans = list.count(3)
print(ans)

# index: return the first index position where the elemtnt appears
names = ['ram','shyam','babu','shyam']
print(names.index('shyam'))

# list looping 
for name in names:
    print(name)

# tuples : Tuple is an ordered, immutable sequence it means 
# indexing availbale and cannt change items after creation
# can store Heterogeneous Data

# tuples are faster and more memory efficient than list why?
# cause Python does not need to reserve extra space for future additions.
# Less memory usage + faster access.

# Lists store extra metadata 
# current size
# allocated capacity
# reference array that can grow
# and dynamic data

tpl = (1,"karn","arjun",4.34,True)
print(tpl)

#tuple paking/Unpaking
tup = ('dip',19,"xyz")
name,age,city = tup
print(name)
print(age)
print(city)

# Swap Variables Easily
x = 7
y = 3
print(x)
print(y)
x,y = y,x
print(x)
print(y)


# t = (10, 20, 30)
# t[1] = 50   # ERROR   

# Where tuple Used in Real projects :
# A) Returning Multiple Values from Functions
def calc(a, b):
    return a+b, a-b

sum1, diff = calc(10, 5)
print(sum1)
print(diff)

# B) Keys in Dictionaries
locations = {
    (23.04, 72.58): "Gandhinagar",
    (23.02, 72.57): "Ahmedabad"
}

# C) Tuples are Used in APIs / Libraries
# Coordinates (x, y)
# RGB values (255, 0, 0)

# ------Tuple Methods (Only Two!)--------

# 1. count()
t = (1,"kaju",True,"kaju","kaju","mumfali")
print(t.count("kaju"))      #<-- unlike lists : here count function returns : number of times element appears

# 2. index()

print(t.index("kaju"))


# SET : Set is an unordered, mutable, unindexed collection of unique elements.
# No duplicates allowed, No indexing, Useful for membership checking

# set = {1,2,2,4,5,6,2,4,5,2,4}
# print(set)  #<- print only unique elemets only

# # Adding items
# set.add(454)
# print(set)

# #removing elements
# set.remove(454)
# set.remove(2)
# print(set)

# Set Operations (very important)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print( set1.intersection(set2) )
print( set1.union(set2) )
print( set1.difference(set2) )
print( set2.difference(set1) )

names = ["alia","raj","smit","himang","raj","kaju","himang"]
unq_names = set(names)
print(unq_names)

# Dictionary : Dictionary is an unordered collection of key-value pairs.
# key must be unique but values can be duplicate 
# keys can be strings,int ,tuple etc

student = {
    "name":"diptesh",
    "age": 19,
    "city" : "xyz"
}
print(student)

# accessing values : (using keys)
print(student['name'])
print(student['age'])

# adding new keys
student['grade'] = "A"
print(student)

#upadting dictionary
student["age"] = 20
print(student)

#remove from dictionary 
student.pop("age")
print(student)

del student['grade']

#looping in ditionary
for key,values in student.items():
    print(key+" : "+values)


# Dictionary methods :

# 1.keys()
info = { 
    "name" : "alia",
    "city" : "xyz",
    "age" : 90,
    "sex" : "female"
}
print(info.keys()) #: returns the number of keys in the dicionary
# print(list(info.keys())) #<--not working cause i created list variable before

# 2.values
print(info.values())

# 3.items()
print(info.items())

# 4.Upadate()

itemss = { 
    "name" : "dip",
    "age" : 19
}
stuff = {
    "age" : 20,
    "city" : "abc"
}

itemss.update(stuff)    #<-- common column updates 
print(itemss)

info.update(country="india")
print(info)

# 5. pop()
info.pop("age")
print(info)

# 6. Clear
info.clear()
print(info)


std = {
    "name" : "dip",
    "marks" : [50,50,50,50] 
}
avg = sum(std["marks"]) / len(std["marks"])
print("average of students : ",avg)

# Excersice : 
# # li = ['keri','safarjan','gvava','pineapple','tarbooch']
# li.append("jaamfad")
# print(li)

# li.remove("pineapple")
# print(li)

# li.sort()
# print(li)

tup = ("aehmedabad","rajkot","gandhinagar","dubai")
print(tup[-1])

li = [1,2,2,3,4,4,5]
unq_val = set(li)
print(unq_val)

diction = {
    "name" : "mosambi",
    "age" : 34,
    "skills" : ["python","java","devOps"]
}
print(diction)
