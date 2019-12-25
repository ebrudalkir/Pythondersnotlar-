import sqlite3
import random
import time
import datetime

con=sqlite3.connect('ebrunundatası.db')
cursor=con.cursor()

def tablooo():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1(zaman REAL,tarih TEXT,anahtarkelime TEXT,deger REAL)")

#tablooo()
def rastgelee():
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime='python sqlite'
    deger=random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1 (zaman,tarih,anahtarkelime,deger)VALUES (?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    con.commit()

def degeral():
    cursor.execute ("SELECT * FROM Tablo1") #burada bütün veriyi çekiyoruz.select zaman tarih dersek sadece onları çeker.belirli
    #satırları almak istersek where deger=2 diğereke sadece bu şekilde olanları çıktı alırız.
    data=cursor.fetchall()
    # print(type(data))# <class 'list'> olduğunu çıktıda görebiliriz.
    #print(data) #şu an veri olmadığı içi boş döndü.Datadak, verileri çıktı olarak döner.
    for i in data:
        print(i) #herbir sğrun sırayla geliyor alt alta



degeral()
con.close()