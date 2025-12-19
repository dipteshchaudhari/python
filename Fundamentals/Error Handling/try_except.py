# try :
#     a = int(input("enter a Number ="))
#     print(10/0)
# except :
#     print("kuch toh gadbad hain!")


# try :
#     a = int(input("enter a number: "))
#     print(a/2)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("Invalid Input")
# else:
#     print("calculation complited")

#Handling multiple Exception togather 

# try : 
#     a = 10 / 0
# except (ZeroDivisionError , ValueError) :
#     print("division by zero or invalid input") 


try : 
    # b = int(input())
    b = 10 / 0
except Exception as e:
    print("Hello, Error accured ",e)


