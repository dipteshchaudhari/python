# example 1:safe calculator

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "cann't divide by zero"

print(divide(10,0))

# example 2

try :
    f = open("data.txt","r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("file not found") 

# example 3
try:
    marks = int(input("etner marks"))
    if marks < 0 or marks > 100:
        raise ValueError
except ValueError:
    print("enter marks between 0-100")

