import random
import time          
kelimeler = ["elma"]
kelime = random.choice(kelimeler)
veri=[]
harfler = []
zaman=5

def kelimeyi_goster():
    print(kelime)

def timer(time):
    
    time.sleep(zaman)
    print(zaman)


def tahmin():
    a=input("kelime giriniz")
    veri.append(a)
    timer(time)
    while(kelime!=a):
        a=input("kelime giriniz")
        veri.append(a)
        timer(time)
 

for harf in veri:
    harfler.append(harf)

print(harfler)  

tahmin()


