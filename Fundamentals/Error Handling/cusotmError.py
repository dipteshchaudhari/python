# example 1:
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


# Example 2
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
