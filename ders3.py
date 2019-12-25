defkullanici="ebru"
defparola="12345"



while (True):
 kullanici = input("enter your username:")
 parola = input("enter your password:")

 if ((defkullanici==kullanici) and (defparola==parola)):
    print("succesfull")
    break
 elif ((defkullanici!=kullanici) and (defparola==parola)):
    print("you entered wrong username!!")
 elif ((defkullanici==kullanici) and (defparola!=parola)):
    print("do you want to change your password? E/H")
    cevap=input()
    if(cevap=="E"):
     yeniparola = input("enter new password")
     print("please waiting")
     defparola=yeniparola
     print("successfull")
 else:
    print("you can try again")
