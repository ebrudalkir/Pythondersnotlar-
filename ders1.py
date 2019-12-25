#a=input("bir syı giriniz:") #kullanıcıdan sayı almak için kullanıyoruz.
#print(a)

#a=input("birinci sayi:")
#b=input("ikinci sayi:")
#c=input("üçüncü sayi:")

#print("sayilarin toplamı:",a+b+c) bu şekilde string olarak gördüğü için yanyana yazıyor.
#print("sayilarin toplamı:",int(a)+int(b)+int(c)) #bu şekilde yazarak bizim istediğimiz sonucu verecektir.
print("Oyuncu kaydetme programı")
ad=input("oyuncunun adı:")
soyad=input("oyuncunun soyadı:")
takim=input("oyuncunun takımı:")

bilgiler=[ad,soyad,takim]

print("Database kaydediliyor....")
#print (bilgiler)
#print("oyuncunun bilgileri:",bilgiler)
print("oyuncunun adı:{}\noyuncunun soyadı:{}\noyuncunun takımı:{}" .format(bilgiler[0],bilgiler[1],bilgiler[2])) #bu şekilde daha simple yazabiliriz.format()
# fonksiyonu içerisinde bu şekilde kullanabiliriz.

print("kaydedildi....")