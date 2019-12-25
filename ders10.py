'''num1=input("enter first number:")
num2=input("enter second number:")

try:
    num1=int(num1)
    num2=int(num2)
    print(num1/num2)
except(ValueError):
    print("error")
except(ZeroDivisionError):
    print("try again")'''

try:
    dosya=open("ebru.txt","r")
except IOError:
    print("it cannot find the file")
finally:
    dosya.closed()

