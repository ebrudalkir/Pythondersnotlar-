def geometri(sekil):
    if len(sekil) == 3:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]

        if (a+b > c) and (a+c > b) and (b+c > a):
            if (a == b) and (a == c) and (b == c):
                print("Eskenar Ucgen")

            elif ((a == b) and (a != c)) or ((a == c) and (a != b)):
                print("Ikizkenar Ucgen")

            else:
                print("Cesitkenar Ucgen")

        else:
            print("Ucgen olusturmaz!")


    if len(sekil) == 4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]

        if (a == b) and (a == c) and (a == d):
            print("Kare")

        elif ((a == b) and (c == d) and (a != c)) or ((a == c) and (b == d) and (a != b)) or ((a == d) and (b == c) and (a != b)):
            print("Dikdortgen")

        else:
            print("Ozel dortgen olusturmaz")

while (True):
    elemanSayisi = int(input("Eleman sayisini giriniz :"))

    if (elemanSayisi == 3):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))

        geometri([a, b, c])

    elif (elemanSayisi == 4):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        d = int(input("d:"))

        geometri([a, b, c, d])

    else:
        print("Gecerli eleman sayisi giriniz!")