# 🐍 Python Fundamentals: 

## **Core Concepts**

### 1. Variables

A **variable** is a name given to a value stored in memory.

* **Rules for Variables:**
    * Must start with a letter or an underscore (`_`).
        * **Valid:** `user`, `_temp`, `age2`
        * **Invalid:** `2age`, `user-name`
    * **Case-sensitive:** `Name` is not the same as `name`.
    * Use **meaningful names** (e.g., `total_price`, not `tp`).

* **Variable Assignment:**
    ```python
    # Standard assignment
    age = 30
    user_name = "Dip"
    
    # You can assign multiple values at once (multiple assignment)
    a, b, c = 10, 20, 30
    ```

### 2. Data Types

Python has several built-in data types. The basic types are:

| Type | Description | Examples |
| :--- | :--- | :--- |
| **Integer** | Whole numbers (positive, negative, or zero) | `10`, `-5`, `200` |
| **Float** | Decimal or floating-point numbers | `10.5`, `3.14` |
| **String** | Sequences of characters, enclosed in quotes | `"Hello"`, `'Python'` |
| **Boolean** | Represents truth values | `True`, `False` |

* **Checking Type:**
    ```python
    x = 10.0
    print(type(x))  # Output: <class 'float'>
    ```

### 3. Operators

Operators are symbols used to perform operations on values and variables.

* **Arithmetic Operators:**
    | Operator | Operation | Example |
    | :--- | :--- | :--- |
    | `+` | Addition | `5 + 2 = 7` |
    | `-` | Subtraction | `5 - 2 = 3` |
    | `*` | Multiplication | `5 * 2 = 10` |
    | `/` | Division (returns float) | `5 / 2 = 2.5` |
    | `%` | Modulo (remainder) | `5 % 2 = 1` |
    | `**` | Exponentiation | `5 ** 2 = 25` |
    | `//` | Floor Division (returns integer) | `5 // 2 = 2` |

* **Comparison Operators (Return `True`/`False`):**
    | Operator | Meaning |
    | :--- | :--- |
    | `==` | Equal to |
    | `!=` | Not equal to |
    | `>` | Greater than |
    | `<` | Less than |
    | `>=` | Greater than or equal to |
    | `<=` | Less than or equal to |

* **Logical Operators:** Combine conditional statements.
    | Operator | Meaning |
    | :--- | :--- |
    | `and` | Returns `True` if both statements are true. |
    | `or` | Returns `True` if one of the statements is true. |
    | `not` | Reverses the result. |

    ```python
    age = 18
    # 18 >= 18 is True AND 18 < 60 is True -> True
    print(age >= 18 and age < 60) 
    ```

### 4. Indentation

**Indentation is the most important part of Python syntax.**

Python uses spaces (usually 4 spaces) to define blocks of code (like the body of a loop or an `if` statement) instead of curly braces (`{}`) used in many other languages.

### 5. Comments

Comments help you explain code and are ignored during execution.

```python
# This is a single-line comment

"""
This is a
multi-line comment
or a docstring 
"""
```

### 6. Naming Conventions (PEP 8)

* **Good Practice (Variables/Functions):** Use **lowercase** characters and **underscores** to separate words (snake\_case).
    ```python
    total_amount = 500
    user_name = "Dip"
    ```

* **Example of Variable Assignment and Type Check:**
    ```python
    a, b, c = 10, 20, 30
    print(a)
    print(type(a))
    
    # Output:
    # 10
    # <class 'int'>
    ```

## **Control Flow**

Control flow determines how your program runs step-by-step based on conditions and repetitions.

The main elements are: `if – else` statements, `loops`, `break`, and `continue`.

### 1. `If – Else` Statements

`If-else` is used to execute code based on whether a condition is `True` or `False`.

* **Using Logical Operators in `If`:**
    ```python
    age = 18 
    country = 'india'
    if(age >= 18 and country == 'india'):
        print("eligible")

    # Output: eligible
    ```

* **`If – Elif – Else` (Chained Conditionals) Example:**
    ```python
    marks = 45

    if marks > 80:
        print("gajab")
    elif marks > 50 and marks < 80 :
        print("good boi")
    else :
        print("Ghee khatam")
        
    # Output: Ghee khatam
    ```

* **Login Example with Chained `If/Elif/Else`:**
    ```python
    Usename = input("Enter your Username = ")
    password = input("Enter Password = ")

    if Usename == 'admin' and password == 'andhenegaanagaya':
        print("Welcome!")
    elif Usename == 'admin' and password == 'password':
        print("correct!")
    elif Usename == 'admin' and password == 'hola':
        print("welcomee")
    else:
        print("Incorrect Password")
    ```

### 2. Loops

Loops are used when you want to repeat a block of code multiple times.

#### A) `For` Loop

Used when you know the number of repetitions or want to iterate over a sequence.

* **Example 1: Loop through a range**
    ```python
    for r in range(10):
        print(f"numbers : {r}")

    # Output: numbers : 0, numbers : 1, ... up to numbers : 9
    ```

* **Example 2: Loop through a list**
    ```python
    list_items = [2.323,"narngi","mosmbi",34,{2,3,4,5}] # Renamed variable 'list' to 'list_items' to avoid overriding built-in 'list'
    
    for lst in list_items:
        print(lst)

    # Output:
    # 2.323
    # narngi
    # mosmbi
    # 34
    # {2, 3, 4, 5}
    ```

#### B) `While` Loop

A `while` loop runs repeatedly as long as its condition remains `True`. **Ensure you update the variable used in the condition to avoid infinite loops!**

```python
num = 1

while num < 10:
    print("numbers printing with while loop",num)
    num=num+1 # Increments num
    
# Output: numbers printing with while loop 1, ... up to numbers printing with while loop 9
```
### 3. `break` Statement

The `break` statement stops the loop immediately, even if the loop's condition is still `True`.

```python
for i in range(10):
    if i == 5:
        break     # Exit the loop entirely
    print(i)
# Output: 0, 1, 2, 3, 4 
# When i == 5, the loop stops.
```
### continue Statement

The continue statement skips the current iteration and goes immediately to the next one.
```python
for i in range(6):
    if i == 3:
        continue    # Skip the print statement for i=3 and jump to the next iteration
    print(i)
# Output: 0, 1, 2, 4, 5
# Number 3 was skipped.
```

### Nested Statements
Nested If
An if statement placed inside another if statement.
```python
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
# Output: Eligible to vote
```

### Nested Loops
A loop placed inside another loop. The inner loop executes completely for every single iteration of the outer loop.
```python
for i in range(3): # Outer loop (i=0, 1, 2)
    for j in range(2): # Inner loop (j=0, 1) runs 3 * 2 = 6 times total
        print(i, j)
```

---

## ⚙️ Functions

### What is a Function?

A function is a block of reusable code that performs a specific task.

Think of a function like a machine:
* You give **input**.
* The machine performs some **action**.
* It **returns output**. 

#### Importance of Functions:
* **Code reusability**: Write once, use many times.
* **Better structure and readability**: Programs are organized logically.
* **Avoid repetition** (DRY principle).
* **Easy debugging and testing**.
* Break large programs into smaller, manageable units.

### 1. Function Definition

Use the `def` keyword to define a function.

```python
def function_name():
    # statements
    pass

# Example: Simple function definition and call
def greet():
    print("hello, brother")

greet() 
# Output: hello, brother
```
### 2. Function Arguments (Parameters)

Arguments are inputs passed to the function to operate on.
```python
def greet(name):
    print("Hello", name)

greet("Alice")
# Output: Hello Alice

```
### 3. Multiple Arguments
Functions can take any number of positional arguments.
```python
def add(a, b):
    print(a + b)

add(5, 7)
# Output: 12
```
### 4. Return Values
Functions use the return statement to send a result back to the caller.
```python
def square(x):
    return x * x

result = square(4)
print(result)
# Output: 16
```

### 5. Default Arguments
You can set a default value for an argument. If the caller doesn't provide a value, the default is used.
```python
def greet_default(name="User"):
    print("Hello", name)

greet_default()      # Uses default value
greet_default("Bob") # Overrides default value

# Output:
# Hello User
# Hello Bob
```
### 6. *args and **kwargs
These are special arguments used when you don't know exactly how many arguments will be passed.

A) *args (Positional Arguments)
Collects multiple positional arguments into a tuple.
```python
def total(*numbers):
    print(numbers)

total(1, 2, 3, 4)
# Output: (1, 2, 3, 4) (A tuple)
```

B) **kwargs (Keyword Arguments)
Collects multiple keyword arguments into a dictionary.
```python
def show_info(**details):
    print(details)

show_info(name="Alice", age=30)
# Output: {'name': 'Alice', 'age': 30} (A dictionary)
```

### 7. Function Types

| Type | Description | Examples |
| :--- | :--- | :--- |
| **Built-in Functions** | Already available in Python. | `print()`, `len()`, `sum()`, `max()`, `type()` |
| **User-Defined Functions** | Functions you create using the `def` keyword. | `greet()`, `add()` |

### 8. Return Multiple Values

Functions can return multiple values, which are automatically packed into a tuple.

```python
def calc(a, b):
    return a + b, a - b

# Unpacking the returned tuple into two variables
sum_result, diff_result = calc(10, 5)

print(f"Sum: {sum_result}, Difference: {diff_result}")
# Output: Sum: 15, Difference: 5
```

### 9. Docstring
A docstring is a description written inside a function (using triple quotes """) to explain what it does.
```python
def greet(name):
    """This function greets the user by their name."""
    print("Hello", name)

# Accessing the docstring:
print(greet.__doc__) 
# Output: This function greets the user by their name.
```
### 10. Scope of Variables
Scope refers to the region of the code where a variable is accessible.

#### Local Scope: A variable declared inside a function is only accessible within that function.
```python
def test_local():
    x = 10  # local variable (only accessible inside test_local)
    print(x)
```
#### Global Scope: A variable declared outside a function is accessible everywhere, including inside functions (unless modified).
```python
x = 5 # global variable
def test_global():
    print(x) # Accessing the global 'x'

test_global() 
# Output: 5
```
### 11. Anonymous (Lambda) Functions
Small, single-line functions created using the lambda keyword. They are restricted to a single expression.

Syntax: lambda arguments: expression

```python
# Lambda function to calculate the square of a number
square_lambda = lambda x: x * x
print(square_lambda(5))
```
Lambda functions are mostly used in:
sorted()
map()
filter()
reduce()

### Simple Calculator

```python
# calculator 

def sum(a,b):
    return a+b
def multi(a,b):
    return a*b
def minus(a,b):
    return a-b
def div(a,b):
    return a/b
a = int(input("enter any number:"))
b = int(input("enter any number:"))
print('Note:please write exact words!!')
op = input("ENter operation [sum,multi,minus,div]]:")

if op == 'sum':
    print("sum = ",sum(a,b))
elif op == 'multi':
    print("multi =",multi(a,b))
elif op == 'minus':
    print("substraction =",minus(a,b))
elif op == 'div':
    print("division= ",div(a,b))
else:
    print("please enter correct operation name!!")
```
### Data Structures in Python
basic Python data structures: lists, tuples, sets, and dictionaries

#### Lists
Ordered, mutable, and dynamic sequences. Indexing is preserved. Size can grow or shrink.
```python
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
```
#### Tuples
Ordered, immutable sequences. Indexing is available, but items cannot be changed after creation. Good for heterogeneous data and fixed collections.

tuples are faster and more memory efficient than list why?
cause Python does not need to reserve extra space for future additions.
Less memory usage + faster access.

Lists store extra metadata 
current size
allocated capacity
reference array that can grow
and dynamic data

```python
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

```
#### Sets
Unordered, mutable collections of unique elements. No indexing. Fast membership checks.

SET : Set is an unordered, mutable, unindexed collection of unique elements.
No duplicates allowed, No indexing, Useful for membership checking

```python
# set creation (duplicates removed automatically)
s = {1, 2, 2, 4, 5, 6}
print(s)  # {1, 2, 4, 5, 6}

# add / remove
s.add(454)
s.remove(454)
s.discard(999)  # no error if element absent

# set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.intersection(set2))  # {3, 4}
print(set1.union(set2))         # {1,2,3,4,5,6}
print(set1.difference(set2))    # {1,2}
print(set2.difference(set1))    # {5,6}

# remove duplicates from a list
names = ["alia","raj","smit","himang","raj","kaju","himang"]
unique_names = set(names)
print(unique_names)

```
#### Dictionaries
Unordered collections of key → value pairs. Keys must be unique and hashable (strings, numbers, tuples, etc.).
Dictionary : Dictionary is an unordered collection of key-value pairs.
key must be unique but values can be duplicate 
keys can be strings,int ,tuple etc

```python
student = {
    "name": "diptesh",
    "age": 19,
    "city": "xyz"
}
print(student)

# access
print(student['name'])
print(student.get('age'))  # safer access (returns None if key missing)

# add / update
student['grade'] = "A"
student['age'] = 20
print(student)

# remove
student.pop("age", None)  # pop with default to avoid KeyError
del student['grade']

# looping
for key, value in student.items():
    print(f"{key} : {value}")
```
Dictionary methods

```python
info = {
    "name": "alia",
    "city": "xyz",
    "age": 90,
    "sex": "female"
}
print(info.keys())    # dict_keys([...])
print(info.values())  # dict_values([...])
print(info.items())   # dict_items([...])

# update / merge
itemss = {"name": "dip", "age": 19}
stuff = {"age": 20, "city": "abc"}
itemss.update(stuff)
print(itemss)

info.update(country="india")
print(info)

# pop / clear
info.pop("age", None)
info.clear()
print(info)  # {}

```
Small examples & exercises

```python
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
```
## TOPIC 5: INPUT / OUTPUT (I/O)

##### USER INPUT 
```python
name = input("Enter your name: ")
print("Hello", name)
```
Taking Multiple Inputs
```python
# a,b = input("Enter values: ").split()
# print(f"values :{a} and {b}")

a,b = map(int, input("enter two Numbers :").split())
print(f"values :{a} and {b}")
```

Evaluating Expressions from Input

```python
exp = eval(input("Enter an Expression :"))
print(exp)
```
##### OUTPUT (PRINT FORMATTING)
f-Strings (Most Important for Developers)

```python
name = "Dip"
age = 19
print(f"My name is {name} and my age is {age}.")
```
Formatting Numbers

```python
pi = 3.14159265
print(f"enter value{pi:.2f}")
print(f"enter value{pi:.4f}")
```
Alignment Formatting (Useful in Reports)
```python
print(f"{'name':10}{'age':5}")
print(f"{'Dip':10}{19:5}")

print(f"{'name':10}{'age':5}")
print(f"{'Dip':10}{'19':5}")
```
##### {'name':10} → print "name" in a field 10 characters wide \n
##### {'age':1} → print "age" in a field 1 character wide

### FILE INPUT / OUTPUT (FILE I/O) :
python can be used to perform operations on a file.(read & write data) 
A file is a named location on disk used to store data permanently. (0,1 bits format)
#### two types of files :
   1.text files : .txt,.docx,.log etc.
   2.Binary Files : .mp4, .png, .mov, .jpeg


Variables store temporary data (lost after program ends), but files store data for future use.
There are three major steps in file handling:
   -Open the file
   -Read / Write the file
   -Close the file
1. Opening a File: open()
```python

file_object = open("filename", "mode")

```
--> Common modes
###### Mode	Meaning
###### "r" --> Read (file must exist)
###### "w"--> Write (overwrite if file exists)
###### "a"--> Append (write at end)
###### "x"--> create a new file and and oper it for writing
###### "b"--> binary mode 
###### "rb"--> Read binary
###### "wb"--> Write binary
###### "r+"--> Read + write
###### "t"--> text mode (defaut)
###### "+"--> open a disk file for updating(reading andd writing) 

2. Closing a File: close()
```python

f.close()

```
### Reading Files
Example : 
```python
f = open("file.txt","r")
data = f.read()
print(data)
f.close() 
```
Read Line by Line
```python
f = open("data.txt", "r")
for line in f:
    print(line.strip())
f.close()

```
READLINE : read one line at a time
```python
f = open("file.txt","r")
data = f.readline()
print(data)

data = f.readline()
print(data)
f.close()

```
Read All Lines into List
```python
f = open("file.txt","r")
data = f.readlines()
print(data)
f.close()   
```
### Writing to Files

-> Write (Overwrites File)
```python
with open("file.txt","w") as f:
    f.write("lata mangeshkar")
```
-> Append to File
```python
with open("file.txt","a") as f:
    f.write("\nAR rehman")
```
--> r+ mode : overwrite the file from the beginning of the file
read + overwrite --> (pointer at start) and (No truncate)
```python
with open("file.txt","r+") as f:

    # f.write("\nkanha")
    # f.write("\ndeven")
    # f.write("\nkrsna")
    # f.write("\ntyla")
    # f.write("\ntylor")

    data = f.read()   #<-- pointer is at y so when we read file it will read after y character in this file
    print(data)
```
--> w+ mode : open for reading and writing , file is creaeted if it doesn't exist otherwise it it truncated
read + overwrite --> truncate 
```python

with open("file.txt","w+") as f :
    print(f.read())
    f.write("this is diptesh!!")
    f.write("\nfile input output")
```

--> a+ mode : pointer place at the end of the string for the appeanding  and when we write something it will appeand the string
read + append data --> (no truncate) (pointer end)   
```python
with open("file.txt","a+") as f:
    f.write("\nusing a+")
    print(f.read())
```
### Breif
r : read the data from a file
w : truncate and write the new data to it 
a : no truncate , append the data at the end
r+ :  read + overwrite --> (pointer at start) and (No truncate)
w+ :  read + overwrite --> truncate 
a+ :  read + append data --> (no truncate) (pointer end)   

### best practice with 'with' statement 
```python
with open("students.txt", "r") as f: 
for line in f: 
print(line.strip())
```
## deleting a file : using os module
module(code library) is a file written by the another programmer,and it generally has 
a functions we can use
   
```python
import os 
os.remove("sample.txt")
```

### some practice 

```python

# practice : create a file with this data 
with open("prac.txt","w") as f:
    f.write("Hi Everyone\n")
    f.write("i am learning file I/o\n")
    f.write("using java\n")
    f.write("and i love java")

# creating a function that replace java with python 

# first we read the data 
with open("prac.txt","r") as f:
        data = f.read()

# then with that data we performed replace operation for replacing python with java
new_Data = data.replace("java", "python")
print(new_Data)

#then we simply overwrite that file with new data 
with open("prac.txt","w") as f:
        f.write(new_Data)
#search the word learning exists in the data or not (function)
def search_word():
    word = "learning"
    with open("prac.txt","r") as f:
        data = f.read()

        if(data.find(word) != -1):
            print("Found that word")
        else:
            print("Not Found") 

search_word()

 # write a function to find in which line of the file the "learning" word occur first

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("prac.txt","r") as f:
        while data:
            data = f.readline()
            if (word in data) :
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()
```

### working with json module : JSON FILE HANDLING

```python
import json

data = {"name" : "dip" , "age" : 19}

with open("data.json","w") as f:
    json.dump(data,f,indent=4)
```
The indent parameter is used to format (pretty-print) JSON data so that it becomes human-readable.

output (without indent)
```python
{"name":"dip","age":19}
```
output (with indent = 4) 
```python
{
    "name": "dip",
    "age": 19
}
```
### CSV File Handling 

```python
import csv

with open("names.csv","r") as f:
    reader = csv.reader(f)

    for line in reader:
        print(line)
```

## CSV & JSON Processing in Python

CSV → tabular data (Excel-like): datasets, logs, reports <br>
JSON → structured, hierarchical data: APIs, configs, web apps

PART 1: CSV PROCESSING <br>
-> CSV = Comma-Separated Values
<br>
name,age,city <br>
Dip,19,Ahmedabad <br>
Raj,20,Surat

#### Reading CSV Files (Basic)

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```
```python
['name', 'age', 'city']
['Dip', '19', 'Ahmedabad']
```

#### Reading CSV as Dictionary
```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```
```python
{'name': 'Dip', 'age': '19', 'city': 'Ahmedabad'}
```

#### Writing CSV Files
```python
import csv

data = [
    ["name", "age", "city"],
    ["Dip", 19, "Ahmedabad"],
    ["Raj", 20, "Surat"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

```
#### Write dictionary-based CSV
```python
import csv

students = [
    {"name": "Dip", "age": 19, "city": "Ahmedabad"},
    {"name": "Raj", "age": 20, "city": "Surat"}
]

with open("students.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(students)

```
### JSON = JavaScript Object Notation

JSON = JavaScript Object Notation
<br> -> Looks like Python dictionaries.
```python
{
  "name": "Dip",
  "age": 19,
  "skills": ["Python", "Java", "SQL"]
}
```

##### Reading JSON Files
```python

import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])
```
##### Writing JSON Files
```python
import json

student = {
    "name": "Dip",
    "age": 19,
    "skills": ["Python", "Java"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```
### Knowing Whether a File Exists or Not:
Sometimes, before reading or writing, you may want to check if a file exists to avoid errors.<br> 
Python provides the os and pathlib modules to check file existence. 
#### Using os.path.exists()

```python
import os 
filename = "students.txt" 
if os.path.exists(filename): 
print(f"Yes, the file '{filename}' exists.") 
else: 
print(f"No, the file '{filename}' does not exist.")
```
#### Using pathlib
```python
from pathlib import Path

file = Path("prac.txt")

if Path.exists(file):
    print("file exists!!")
else:
    print("file not found !!")

```

# error Handling in python
This topic is critical because real programs fail, and professional developers know how to handle<br> failures gracefully instead of crashing.
We will cover:

1) What errors are
2) Types of errors
3) try / except
4) else / finally
5) Handling multiple exceptions
6) Raising exceptions
7) Custom exceptions
8) Real-world examples
9) Best practices

### 1) What is an Error?
An error is a problem that occurs during program execution and stops the program if not handled.
```python
x = 10 / 0
```
ZeroDivisionError

### 2. Types of Errors in Python
##### A) Syntax Error (cannot be handled) <br>
-> Occurs before execution. <br>
-> You must fix the code.<br>

##### B) Runtime Errors (can be handled) 

Common ones:
1) ZeroDivisionError : division by error : 10/0
2) ValueError : ValueError occurs when a function gets a value of the right type but an invalid value. ex :int("abc")
3) TypeError : incompatible data type. ex :"10" + 5
4) IndexError : occurs when you try to access an index that is outside the valid range of a sequence
5) KeyError : occurs when you try to access a dictionary key that does not exist.
6) FileNotFoundError : occurs when Python tries to open a file that does not exist at the specified path. ex : f = open("data.txt", "r")
These are what try–except handles.

### 3. try / except (Core Concept)

Basic Syntax
```python
try:
    # risky code
except:
    # runs if error occurs

```
```python
try:
    a = int(input("Enter a number: "))
    print(10 / a)
except:
    print("Something went wrong")
```
Using this program does not crash

### 4. Catching Specific Exceptions (VERY IMPORTANT)
```python
try:
    x = int(input())
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

```
### 5. else Block
```python
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Division by zero")
else:
    print("Calculation successful")
```
### 6. finally Block

finally block is used with try–except to define code that must execute no matter what, whether an exception occurs or not.

```python
try:
    # code that may raise an error
except SomeError:
    # code that runs if an error occurs
finally:
    # code that always runs

```
Example :
```python
try :
    x = int(input("Enter a Number:"))
    print(x/0)
except ZeroDivisionError:
    print("can not divide by zero")
finally : 
    print("this block always execute")
```
Example :
```python
try :
    f = open("name.txt","r") 
    print(f.read())
except FileNotFoundError:
    print("file not found")
finally : 
    f.close()  #if file exists this execute 
    print("file closed")
```
### Handling Multiple Exceptions Together
```python
try:
    # code that may raise errors
except (ErrorType1, ErrorType2):
    # common handling code

```
```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(result)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")
```
Catching all exceptions together
```python
try : 
    # b = int(input())
    b = 10 / 0
except Exception as e:
    print("Hello, Error accured ",e)
```
### Raising Exceptions (raise)
raise keyword is used to manually trigger an exception. This is useful when you want to enforce rules, validate data, or signal that something is wrong in your program.

Example 1:
```python
age = int(input("enter any age:"))

if age < 18:
    raise ValueError("age must be 18 or above 18")
else:
    print("access granted")
```
Example 2:
```python
try :
    num = int(input("enter a Number:"))
    if num == 0:
        raise ZeroDivisionError("Zero se devide nahi hoga")
    print(10/num)
except ZeroDivisionError as e:
    print("Error is :",e)
```
### Custom Exceptions
 use exception class :
```python
class InvalidAgeError(Exception):
    pass
```
Example 1:
```python
class BalanceError(Exception):              #custom error
    pass
try:
    balance = 1000                  
    withdraw = int(input("enter your amount : "))

    if withdraw > balance:
        raise BalanceError("Insufficient balance")

    balance -= withdraw

    print("remaining balance",balance)
except Exception as e:
    print("ye toh Error hain:",e)
```
example 2:
```python
class usernameError(Exception):
    pass
class PassError(Exception):
    pass


try :
    username = input("enter username:")
    password = input("enter password:")

    if(username != 'admin'):
        raise usernameError("invalid username")
    if(password != 'raju'):
        raise PassError("invalid password")
except (usernameError , PassError) as e:
    print("Login failed :",e)

else:
    print("login successful")   
```
### Examples
example 1:
```python
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "cann't divide by zero"

print(divide(10,0))
```
example 2:
```python
try :
    f = open("data.txt","r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("file not found") 
```
example 3:
```python
try:
    marks = int(input("etner marks"))
    if marks < 0 or marks > 100:
        raise ValueError
except ValueError:
    print("enter marks between 0-100")
```

### Where Error Handling is Used
1) File operations
2) APIs & web apps
3) Data validation
4) Machine learning pipelines
5) Automation scripts
6) User input handling

### Best Practices
✔ Catch specific exceptions
✔ Keep try block small
✔ Use finally for cleanup
✔ Raise meaningful errors
✔ Never silence errors blindly
