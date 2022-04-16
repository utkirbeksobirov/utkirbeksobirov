def talabalar(ism, familya, **malumotlar):
    """Talabalarning Ism Familyasini Qaytaruvchi Funksiya"""
    malumotlar['ism'] = ism
    malumotlar['familya'] = familya
    return malumotlar
talaba1 = talabalar('Ismoil', 'Xojiyev', oqish_joyi='bogcha', yoshi=16)
talaba2 = talabalar('Utkir', 'Sobirov', oqihs_joyi='unversitet', yoshi=18)

print(talaba1)

def avto_kirit(kompaniaya, model, karobka, rangi, narhi=None):
    avto = {
        'kompaniaya':kompaniaya,
        'model':model,
        'karobka':karobka,
        'rangi':rangi,
        'narhi':narhi

    }
    return avto




def avto_info():
    avtolar = [] 
    while True:
        kompaniya = input("Kompaniyasini Kiriting: ")
        mod = input("Modelini Kiriting: ")
        karob = input("Karobkani Kiriting: ")
        rang = input("Rangini Kiriting: ")
        savol = input("Yana Mashina Tanlaysizmi (yes or no): ")
        avtolar.append(avto_info(kompaniya, mod, karob, rang))
        if savol == 'no':
            break
        return avto_info

def avto_print(avto_info):
    print(
        f"{avto_info}[kompaniya.title()]  {avto_info}[mod.title()] {avto_info}[karob.title()]"
        f"{avto_info}[rang.title()]"

    )

import math


uzunlik = lambda pi, r: 2*pi*r
print(uzunlik(math.pi,10))

kvadrat = lambda x, y : x ** y
print(kvadrat(3, 2))

def daraja(n):
    return lambda x: x ** n

kvadrat = daraja(2)
kub = daraja(3)
print(kvadrat(20))


from math import sqrt

sonlar = list(range(11))
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)

def daraja2(x):
    """###"""
    return x*x

print(list(map(daraja2,sonlar)))

kvadratlar = list(map(lambda x: x * x, sonlar))
print(kvadratlar)

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y: x + y, a, b))
print(a_plus_b)


ismlar = ['husan', 'hasan', 'ismoil', 'utkir']
print(list(map(lambda matn: matn.upper(), ismlar)))


import random as r

sonlar = r.sample(range(100), 10)
def juftmi(x):
    return x % 2 == 0

juft_sonlar = list(filter(juftmi,sonlar))
print(juft_sonlar)                                 


mevalar = ['anor', 'olma', 'banan', 'nok', 'behi', 'tarvuz', 'anjir', 'shaftoli']
harf = 'a'
mevalar_b = list(filter(lambda meva: meva.startswith (harf), mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda mevalar: len(mevalar) <= 5, mevalar))
print(mevalar2)

list(filter(lambda meva: (meva.startswith('a') and meva.endswith('r')), mevalar))

sonlar = r.sample(range(100), 10)
juft = [son for son in sonlar if son%2==0]

