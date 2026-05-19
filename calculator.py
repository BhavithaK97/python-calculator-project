def add(a,b): 
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b   
def division(a,b):
    if b==0:
        return "Cannot divided by zero"
    return a/b
print("Select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter chioce (1 or 2 or 3 or 4:)"))
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
if choice==1:
    print("Result is:",add(a,b))
elif choice==2:
    print("Result is:",subtract(a,b))
elif choice==3:
    print("Result is:",multiply(a,b))
elif choice==4:
    print("Result is:",division(a,b))
else:
    print("Invalid choice")
