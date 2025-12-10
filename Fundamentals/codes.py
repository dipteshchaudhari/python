a,b,c = 10,20,30
print(a)
print(type(a))

age = 18 
country = 'india'
if(age >= 18 and country == 'india'):
    print("eligible")

marks = 45

if marks > 80:
    print("gajab")
elif marks > 50 and marks < 80 :
    print("good boi")
else :
    print("Ghee khatam")


for r in range(10):
    print(f"numbers : {r}")

list = [2.323,"narngi","mosmbi",34,{2,3,4,5}]

for lst in list:
    print(lst)


num = 1

while num < 10:
    print("numbers printing with while loop",num)
    num=num+1

for i in range(10):
    if i == 5:
        break       #exist the whole loop when break statement hits
    print(i)

for i in range(10):
    if i == 5:
        continue    #skips the current iteration only 
    print(i)


#Nested if
age = int(input("ENter YOur age : "))
country = input("COuntry ? : ")
if age >= 18 :
    if country == 'india':
        print("Eligible fot vote in India!!")
    elif country == 'Afganistan':
        print("Eligible for vote in Afganistan!!")
    else:
        print("Check Your nationlity , brother or sister")
else:
    print("Ur Under-Age, bade hoke aao")


# Nested Loop 

for i in range(5):
    for j in range(4):
        print(i,j)


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


