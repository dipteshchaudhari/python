import math
import random
import datetime
import os
import sys
import json

#math module : Used for mathematical operations.
print(math.sqrt(64))
print(math.factorial(3))

#random module : Used to generate random values.
print(random.randint(1,100))

#datetime module : Used for date and time operations.
print(datetime.datetime.now())

# os module : Used to interact with the operating system.
print(os.getcwd())

# sys : Used for system-specific parameters.
print(sys.version)

# json : Used to work with JSON data.
data = {'name':'dip','age':19}
print(json.dumps(data))