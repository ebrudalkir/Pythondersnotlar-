
'''for i in range(1,10):
    print(i*"*")'''
factoriyel=1
while True:
    sayi=int(input("enter of numbers:"))
    if(sayi<=0):
        print("please enter positive number!!")

    else :
        for i in range(1,sayi+1):
            factoriyel=factoriyel*i
        print("factoriyel",factoriyel)
        break


