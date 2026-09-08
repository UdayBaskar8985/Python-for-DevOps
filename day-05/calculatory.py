import sys

def add(num1, num2):
    addition = num1+num2
    return addition

def sub(num1, num2):
    subtraction = num1 - num2
    return subtraction
    
def mul(num1, num2):
    multiplication = num1*num2
    return multiplication
    
num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
    print(output)
    

if operation == "sub":
    output = sub(num1, num2)
    print(output)
    
if operation == "mul":
    output = mul(num1, num2)
    print(output)