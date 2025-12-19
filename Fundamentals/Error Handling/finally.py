try :
    x = int(input("Enter a Number:"))
    print(x/0)
except ZeroDivisionError:
    print("can not divide by zero")
finally : 
    print("this block always execute")


try :
    f = open("name.txt","r") 
    print(f.read())
except FileNotFoundError:
    print("file not found")
finally : 
    f.close()  #if file exists this execute 
    print("file closed")

