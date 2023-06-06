import random
import time  
from itertools import combinations

kelimeler = ["elma"]
kelime = random.choice(kelimeler)
veri=[]
harfler = []
zaman=1
kombinasyonlar = []

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

    birlesik_veri ="".join(veri)
    print(birlesik_veri)
    for harf in birlesik_veri:
        temp=list(harf)
        harfler.append(temp)
    print(harfler)
    
    
tahmin()