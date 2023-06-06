import random
import time  
from itertools import permutations

kelimeler = ["elma"]
kelime = random.choice(kelimeler)
veri=[]
harfler = []
zaman=1
permutasyonlar = []

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
    

    for r in range(1, len(birlesik_veri) + 1):
        permutasyonlar.extend(permutations(birlesik_veri, r))

    for permütasyon in permutasyonlar:
        print(birlesik_veri[1]+birlesik_veri[0]+''.join(permütasyon))
    
tahmin()