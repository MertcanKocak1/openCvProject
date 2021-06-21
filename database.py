import sqlite3
from datetime import datetime

simdi = datetime.today()
current_time = simdi.strftime("%H:%M:%S")
current_date = simdi.strftime("%d-%m-%y")
try:
    with sqlite3.connect("C:\\Users\\inuxe\\OneDrive\\Desktop\\Bitirme Projesi\\aracListesi.db") as conn:
        cursor = conn.cursor()
except Exception as e:
    print(e)
    print("Database'e Bağlanırken Sorunla Karşılaşıldı")


def aracGirisi(plaka):
    veriler = cursor.execute(f"""Select * from Araclar where Plaka = '{plaka}'""")
    id = -1
    for row in veriler:
        id = row[0]
    if id != -1:
        cursor.execute(f"""INSERT INTO Giris (Arac, Saat , Gun) VALUES ({id},'{current_time}','{current_date}')""")
        print("Kapı Açılıyor")
        conn.commit()
    else:
        print("Veritabanında kayıtlı değilsiniz giriş yapamayacaksınız" , plaka)


def aracEkle(aracSahibi, plaka, model):
    cursor.execute(
        f"""INSERT INTO Araclar (AracSahibi , Plaka , AracModel) VALUES ("{aracSahibi}" , "{plaka}","{model}")""")
    conn.commit()


def aracSil(id):
    cursor.execute(f"delete from Araclar where id = {id} ")
    conn.commit()


def girisKaydıGetirTekArac(id):
    kayıtlar = cursor.execute(f"select * from Giris where Arac = {id}")
    return kayıtlar


def zamanaGöreKayıtGetir(tarih1, tarih2):
    record = -1
    kayıtlar = conn.execute(f"select * from Giris where Gun between '{tarih1}' and '{tarih2}'")
    for kayıt in kayıtlar:
        record = kayıt[0]
        break
    if record == -1:
        return -1
    else:
        return kayıtlar


def plakayaGöreAracBul(plaka):
    arac = conn.execute(f"select * from Araclar where Plaka = '{plaka}'")
    aracId = -1
    for row in arac:
        aracId = row[0]
    return aracId


def idyeGöreAracBul(id):
    arac = conn.execute(f"select * from Araclar where ID = {id} ")
    aracPlaka = -1
    for row in arac:
        aracPlaka = row[2]
    return aracPlaka
