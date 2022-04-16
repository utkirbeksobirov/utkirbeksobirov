class Talaba:
      """Talaba Nomli Class Yaratamiz"""

      def __init__(self, ism, familya, t_yil):
        self.ism = ism
        self.familya = familya
        self.t_yil = t_yil

      def tanishtir(self):
        print(f"Ismim {self.ism} Familyam {self.familya} {self.t_yil} da Tug'ilganman")


talaba1 = Talaba('Utkir', 'Sobirov', 2004)
talaba2 = Talaba('Ismoil', 'Xojiyev', 2006)
print(talaba1.ism)




class Talaba:
    """Yangi Class"""

    def __init__(self, ism, familya, t_yil):
        self.ism = ism
        self.familya = familya
        self.t_yil = t_yil

    def get_name(self):
        return self.ism

    def last_name(self):
        return self.familya

    def full_name(self):
        return f"{self.ism} {self.familya}"

    def get_age(self, yil):
        return yil - self.t_yil
talaba1 = Talaba('Utkir', 'Sobirov', 2004)
talaba2 = Talaba('ismoil', 'Xojiyev', 2006)

print(talaba1.get_age(2022)) 
print(talaba1.full_name()) 

def son():

    a = int(input("1-Sonni Kiriting: "))
    b = int(input("2-Sonni Kiriting: "))
    c = int(input("3-Sonni Kiriting: "))
    if a > b and c:
        print(f"{a} Soni Katta {b} va {c} dan")

    elif b > c and a:
        print(f"{b} Soni Katta {a} va {c} dan")

    elif c > a and b:
        print(f"{c} Soni Katta {a} va {b} dan")

son()


class Talaba:


    def __init__(self, ism, familya, tyil):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
        self.bosqich = 1

    def get_name(self):
        return self.ism

    def get_info(self):
        return f"Mening Ismin {self.ism} Familyam {self.familya} Men {self.tyil} da Tug'ilganman"

    def set_bosqich(self, bosqich):
        self.bosqich = bosqich

    def update_bosqich(self):
        self.bosqich += 1

    def get_lastname(self):
        return self.familya
    

    def get_year(self):
        return self.tyil

    def tanishtir(self):
        return f"Salom Mening Ismim {self.ism} Familyam {self.familya} Men {self.bosqich} Bosqich Talabasiman" 

talaba1 = Talaba('Utkir', 'Sobirov', 2004)
print(talaba1.get_info())
talaba1.update_bosqich()
print(talaba1.tanishtir())
        




class Fan:
    
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_students(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1


    def  get_name(self):
        return self.nomi

    def get_students(self):
        return [talaba.get_fullname() for talaba in self.talabalar]

    def get_students_num(self):
        return self.talabalar_soni

matematika = Fan("Dasturlash")
talaba1 = Talaba('Ismoil', 'Xojiyev', 2006)
talaba2 = Talaba('Samandar', 'Raxmonqulov', 2005)
talaba3 = Talaba('Ismoil', 'Allayorov', 2004)
matematika.add_students(talaba1)
matematika.add_students(talaba2)
matematika.add_students(talaba3)

son = int(input("Son Kiriting: "))
print(son = son)

from uuid import uuid4

class Mashina:
   
    __num_avto = 0
    
    def __init__(self, modeli, rangi, yili, narx, km=0):
        self.modeli = modeli
        self.rangi = rangi
        self.yili = yili
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Mashina.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto    

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:  
            print("Mashinani Km Kamaytirib Bo'lmaydi! ")

avto1 = Mashina('Malibu', 'Oq', 2020, 20000)                    

class Talaba: 
    def __init__(self,ism,familya,tyil):
        self.ism = ism
        self.familya = familya 
        self.tyil = tyil
        self.bosqich = 1
    def get_info(self):        
        return f"{self.ism} {self.familya} {self.tyil} yilda tugilgan {self.bosqich}-bosqich talabasi"
    def set_bosqich(self,bosqich):
        self.bosqich = bosqich
    def update_bosqich(self):
        self.bosqich += 1

talaba1 = Talaba('Alijon', 'VAliyev', 2000)
print(talaba1.get_info())
talaba1.update_bosqich()
print(talaba1.get_info())


class Avto:
    __num_avto = 0
    
    def __init__(self, make, model, yili, karobka, narx):
        self.make = make
        self.model = model
        self.yili = yili
        self.karobka = karobka
        self.narx = narx
        Avto.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.Avto
    
    def __repr__(self):
        return f"Avto: {self.make} {self.model} {self.narx}"

    def __gt__(self, boshqa_avto):
        return self.narx > boshqa_avto.narx
    
    def __lt__(self, boshqa_avto):
        return self.narx < boshqa_avto.narx
    
    
    def get_make(self):
        return self.make
   
    def get_model(self):
        return self.model
    
    def get_yili(self):
        return self.karobka
    
    def get_narx(self):
        return self.narx
    
avto = Avto('BMV', 'X9', 2021, 'Avtomat', 90000)
avto1 = Avto('BMV', 'X7', 2020, 'Avtomat', 70000) 


class AvtoSalon:
    
    def __init__(self, name):
        self.name = name
        self.avtolar = []
    
    
    def __repr__(self):
        return f"{self.name} avto saloni"
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self, index):
        return self.avtolar[index]
    
    
    def __setitem__(self, index, value):
        if isinstance(value, Avto):
            self.avtolar.append(avto)
        self.avtolar[index] = value
        
    def __call__(self, *param):
        if param:
            for avto in param:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
        
    def __add__(self, qiymat):
        if isinstance(qiymat, AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} {qiymat.name}")    
            yangi_salon_avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat, Avto):
            self.add_avto(qiymat)
        else:
            print(f"AvtoSalonga  {type(qiymat)} Qo'shib Bo'lmaydi")
            
            
            
    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto Obyektini kiriting !")
                
    def get_list(self):
        return [avto for avto in self.avtolar]            
                

salon1 = AvtoSalon("GM")
salon2 = AvtoSalon("Uz Gm")
salon3 = AvtoSalon("Uz Motor")



import random
def son(x = 10):
        t_son = random.randint(1, x)
        print(f"Men 1dan {x}gacha Son O'yladm Siz Uni Topa Olasizmi")
        taxminlar = 0
        while True:
            taxminlar += 1
            son = int(input((">>> ")))
            if son < t_son:
                print(f"Yo'q Men O'ylagan Son {son}dan Kattaroq ")
            elif son > t_son:
                    print(f"Yo'q Men O'ylagan Son {son}dan Kichikroq ")
            else:
                print(f"Tabriklayman Siz Sonni Topdingiz {taxminlar}ta Taxmin bn Topdiz")
                break

from ursina import *
from ursina.prefabs.first_person_controller import FirstPerson

app = Ursina()
ground = Entity(model = 'plane',
                texture = 'grass',
                collider = 'mesh',
                scale = (100, 1, 100))
player = FirstPersonController()
Sky()
mybox = Entity(model = 'cube',
                color = 'black',
                collider = 'box',
                position = (5, 0.5))
app.run            

def hafta():
    
    switcher = {
        1: "Dushanba",
        2: "Seshanba",
        3: "Chorshnba",
        4: "Payshnba",
        5: "Juma",
        6: "Shanba",
        7: "Yakshnba"
        
    }

yosh = input("Tug'ulgan Yilingizni Kiriting: ")
try:
    yosh = int(yosh)
    print(f"Sizning Yoshingiz {2022-yosh} Yosh")
except ValueError:
    print("Iltimos butun Son Kiriting! ")
    
mevalar = ['olma', 'anor', 'anjir', 'uzum']
a = int(input("Kiriting: "))
index = a - 1
try:
    if len(mevalar) <= index:
        print(mevalar[index])
except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta Meva Bor")
else:
    print(mevalar(index))

user = {"username": "jatlx",
        "status": "admin",
        "email": "utkirsobirov2000@gmail.com",
        "phone": "88 908 82 83"}
key = "phone"
try:
    print(f"Foydalanuvchi: {user[key]}")
except KeyError:
    print("Bunday Kalit So'z Mavjud Emas")                     

with open("index.txt") as file:
    pi = file.read()
# print(pi)

pi = pi.rstrip()
pi = pi.replace("\n", "")
pi = float(pi)
print(pi)

filename = "file/index.txt"
with open(filename) as file:
    for line in file:
        print(line)

with open(filename) as file:
    index = file.readlines()

print(index)

indexx = [index.rstrip() for index in index]
print(index)

faylnomi = "new_file.txt"
ism = "Utkir Sobirov"
t_yil = 2004
with open(faylnomi, "w") as fayl:
    fayl.write(ism + "\n")
    fayl.write(str(t_yil) + "\n")

with open(faylnomi, "a") as fayl:
    fayl.write("Ismoil Xojiyev\n")
    fayl.write("2006")

import pickle

talaba1 = {"ism": "Utkir", "familya": "Sobirov", "t_yil": 2004, "kurs": 2}

import json 

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

ism = "Utkir"
ism_json = json.dumps(ism)
familya_json = json.dumps("Sobirov")

sonlar = (12, 42, 57, 44)
sonlar_json = json.dumps(sonlar)
       
a = 12
b = 5
print(f"b = {a}, a = {b}")


bemor = {
    "ism": "Ismoil Xojiyev",
    "yosh": 16,
    "oila": False,
    "farzandlari": ("Yuq"),
    "allergiya": None,
    "dorilari": [
            {"nomi": "Validol", "Miqdori Kuniga": 2},
            {"nomi": "Trimol", "Miqdori Kuniga": 5}
        ],
    
    }

bemor_json = json.dumps(bemor)
print(bemor_json)

with open("sonlar_json" "w") as f:
    json.dumps(sonlar, f)


bemor2 = json.loads(bemor_json)
print(bemor2)

filename = "bemor.json"
with open(filename) as f:
    bemor = json.load(f)
    
print(type(bemor))    


