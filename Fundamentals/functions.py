def greeting(name):
    print(f"Hello {name} bhai ! hola amigo ! kese ho thik ho!")
greeting("kanha")

def do_calculations(a,b,c,d,f,g):
    print("Exp1:",a/b-c*d)
    print("Exp2:",a/c-5)
    print("Exp3:",a-d/g*f)
do_calculations(1,2,4,3,5,6)

def return_value(a,b):
    return a/b-a-5**2

ans = return_value(2,3)
print("Answer : ",ans)

def say_hola(name="bhaiya"):
    print(f"Hola, {name}")
say_hola("kanti")
say_hola()

def do_sum(*args):
    # ans = sum(args)
    # return ans
    sum = 0
    for num in args:
        sum = sum + num
    return sum

print(do_sum(1,2,3,4))

def keyword_args(**kwargs):
    print(kwargs)
    for key,value in kwargs.items() :
        print(key ,":",value )
keyword_args(name='ram',age=1000,city='rampur')

# return multiple values 
def calcu(a,b):
    return a+b,a-b
print(calcu(4,5))
 
# docstring : Docstring is a description written inside a function to explain what it does.

def thank(name='kaju'):
    '''this function says thank you'''
    print(f"thank you ,{name}")
thank("mahesh")
print(thank.__doc__) #<-- for reading doccstring   fun_name.__doc__ 

# Lamnbda function

square = lambda x : x**2
print(square(4))

multi = lambda a,b : a*b
ans = multi(34,22)
print(ans)

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