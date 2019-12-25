#ilk önce ardışık sayı bulma fonksiyonunu yazalım

'''def primenumber():
    c=0
    x=int(input("enter a number:"))
    for i in range (2,x):
        if(x%i==0):
            c=1;

    if(c==1):
        print("not a prime number")
    else:
        print("yes prime number")

primenumber() fonskiyon mantığıyla çağırdık.


while(True): buradada döngü içerisinde yazdık.
    c=0
    x=int(input("enter a number:"))
    for i in range (2,x):
        if(x%i==0):
            c=1;

    if(c==1):
        print("not a prime number")
    else:
        print("yes prime number")'''



def primenumber():
    x=int(input("enter first vale of range:"))
    y=int(input("enter second vale of range:"))
    for i in range (x,y+1):
        for j in range(2,i):
            if(i%j ==0):
                break
        else:
            print(i)

primenumber()

'''sayi1 = int(input("Sayı 1: "))
sayi2 = int(input("Sayı 2: "))

print(sayi1, "ile", sayi2, "arasındaki asal sayılar:")

for sayi in range(sayi1, sayi2 + 1):
    if sayi > 1:
        for i in range(2, sayi):
            if (sayi % i) == 0:
                break
        else:
            print(sayi)'''


