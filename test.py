import random
import time          
kelimeler = ["elma", "armut", "muz", "portakal", "çilek", "kiraz", "ankara"]
kelime = random.choice(kelimeler)
zaman=5

def kelimeyi_goster():
    print(kelime)

def timer(time):
    
    time.sleep(zaman)
    print(zaman)


def tahmin():
    a=input("kelime giriniz")
    timer(time)
    while(kelime!=a):
        a=input("kelime giriniz")
        timer(time)
tahmin()

