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
