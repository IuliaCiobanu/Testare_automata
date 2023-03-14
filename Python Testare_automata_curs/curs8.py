# CEI 4 PILONI OOP

# 1.MOSTENIREA
# class Chef:
#     cutite=None
#     linguri=None
#     def __init__(self, nr_cutite):
#         self.cutite=nr_cutite
#     def make_salad(self):
#         print("salad")
#     def make_fries(self):
#         print("fries")
#
# class Chef2:
#     sort=2
#
# class JapaneseChef(Chef):
#     def __init__(self, cantitate_alge, cutite):
#         self.alge=cantitate_alge
#         self.cutite=cutite
#     def make_sushi(self):
#         print("sushi")
#
# # o clasa poate mosteni din mai multe clas
# class ItalianChef(Chef,Chef2):
#     tava=1
#     def make_pizza(self):
#         print("pizza")
#
# new_chef=Chef(3)
# new_chef.make_fries()
#
# japan=JapaneseChef(10,5)
# japan.linguri=6
# print(japan.linguri)
# japan.make_sushi()
# italian=ItalianChef(4)
# italian.tava=8
# italian.linguri=7
# print(italian.tava, italian.sort, italian.linguri)
#
# class TokyoChef(JapaneseChef):
#     alge=300
#
#
# tokyo=TokyoChef(10,5)
# print(tokyo.linguri)

# ////////////////////////////

# class Animale:
#     sunete=None
#     culoare=None
#     specie=None
#     varsta=0
#     sunet_somn_mancare=None
#     def dorm(self):
#         print(f"Acum dorm {self.sunet_somn_mancare}")
#     def imbatranire(self):
#         self.varsta+=1
#         print(f"Acum am {self.varsta}")
#
# class Pisica(Animale):
#     toarce="da"
#     vaneaza_soareci=None
#     def toarce_sa_ceara_mancare(self):
#         if self.toarce=="da":
#             self.sunet_somn_mancare="miau"
#             print(self.sunet_somn_mancare)
#
# pisica=Animale()
# pisica_mostenitoare=Pisica()
# pisica.sunete="miau miau"
# print(pisica.sunete)
# print(pisica_mostenitoare.sunete)
#
# pisica.dorm()
# pisica.sunet_somn_mancare

# pisica_mostenitoare.dorm()
# pisica_mostenitoare.sunet_somn_mancare()

# POLIMORFISM
# a) PRIN FUNCTII CU NR INDEFINIT DE PARAMETRII
#    ex:functia len(), functie(*args),functie(**kwargs)

# def suma(*args):
#     s=0
#     print(type(args))
#     # s = s + args
#     for elem in args:
#         s=s+elem
#     print(s)
#
# suma(2,3,4)
# suma(2,3,4,10)
# suma(2,3,4,10,11)

# parametrii initializati cu valoare default:
# def add(x,y=0,z=1):
#     return x+y+z
# print(add(5))
# print(add(5,7))
# print(add(5,7,8))

# b)implementarea aceleiasi metode in clase diferite
# class America:
#     imn="imnul americii"
#     limba="americana"
#     drapel="american"
#     def printeaza_limba(self):
#         print(f"limba este {self.limba}")
#
# class Romania:
#     imn="imn romanesc"
#     limba="romana"
#     drapel="tricolor"
#     def printeaza_limba(self):
#         print(f"limba este {self.limba}")
#
# america=America()
# romania=Romania()
# america.printeaza_limba()
# romania.printeaza_limba()

# c)Reimplementare/rescriere metodei din calsa mama in clasa copil- Pasare/Pinguin - metoda zboara:
# class Pasare:
#     def describe(self):
#         print("sunt o pasare")
#     def zboara(self):
#         print("sunt o pasare deci zbor")
#
# class Papagal(Pasare):
#     def vorbeste(self):
#         print("vorbesc deci sunt papagal")
#
# class Pinguin(Pasare):
#     def zboara(self):
#         print("sunt papagal si nu zbor")
#
# pasare=Pasare()
# pasare.describe()
# pasare.zboara()
# print("************************")
# papagal=Papagal()
# papagal.describe()
# papagal.zboara()
# papagal.vorbeste()
# print("************************")
# pinguin=Pinguin()
# pinguin.describe()
# pinguin.zboara()


# exemlplu suplimentar
class Chef():  # clasa parinte
    cutite = None
    linguri = None
    def __init__(self, nr_cutite): # constructor cu 1 parametru
        self.cutite = nr_cutite
    def make_salad(self):
        print("salad")
    def make_fries(self):
        print("fries")

class Chef2():  # clasa parinte, doar cu un singur atribut, fara constructor sau metode
    short = 2

class JapaneseChef(Chef):
    def __init__(self, cantitate_alge, cutite):
        self.alge = cantitate_alge
        self.cutite = cutite
    def make_sushi(self):
        print("sushi")

class ItalianChef(Chef, Chef2):
	tava = 1
	def make_pizza(self):
		print("pizza")

print("-------------------------------")
# aici instantiem un obiecte de tipul clasei parinte
newChef = Chef('6')
newChef.make_fries()
print("-------------------------------")
nakamoto = JapaneseChef(5, 3)
nakamoto.linguri = 56
print(nakamoto.linguri)
nakamoto.make_sushi() # apelam functia din clasa copil
nakamoto.make_salad() # apelam functia din clasa parinte
print("-------------------------------")

mario = ItalianChef('12') # trebuie sa ii dam ca si argument nr de cutite => datorita constructorului din clasa Chef din care mosteneste
print(mario.tava) # printam valoarea atributului din clasa copil
print(mario.linguri) # printam valoarea atributului din clasa parinte Chef
print(mario.short) # printam valoarea atributului din clasa parinte Chef2

print("-------------------------------")
class TokioChef(JapaneseChef): # clasa copil TokioChef mosteneste de la clasa parinte JapaneseChef, care la randul ei
							   # mosteneste de la clasa ei parinte Chef
	alge = 300

tokyo=TokioChef(3,4)
print(tokyo.cutite)

print("-------------------------------")
class Animale():
		sunet = None
		culoare = None
		specie = None
		rasa = None
		varsta = None
		sunet_somn_mancare = None
		greutate = None
		culoare_ochi = None

		def dormi(self):
				print(f"Acum dorm: {self.sunet_somn_mancare}")

		def mareste_varsta(self):
				self.varsta += 1
				print(f"Acum am {self.varsta} ani")

pisica = Animale()
pisica.sunet = "miau"
pisica.culoare = "portocaliu"
pisica.varsta = 2
pisica.sunet_somn_mancare = "prrrrrr"
pisica.dormi()
pisica.mareste_varsta()