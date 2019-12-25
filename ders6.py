"""def hello():
    print("hello world")

hello()"""
def factorial(num):
    fact=1
    for i in range(1,num+1):
       fact=fact*i
    print("factorial:",fact)
    #return fact

x=int(input("enter a number:"))
a=factorial(x)
print(a)



