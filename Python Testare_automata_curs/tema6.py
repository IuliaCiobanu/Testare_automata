"""Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute

Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""
# class Cerc:
#     raza = 5
#     culoare = "galben"
#     def descrie_cerc(self):
#         print(f"raza: {self.raza}, culoare:{self.culoare}")
#     def aria(self):
#         return 3.14*self.raza
#     def diametru(self):
#         return 2*self.raza
#     def circumferinta(self):
#         return 2*3.14*self.raza


"""2. Clasa Dreptunghi
Atribute: lungime, latime, culoare Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. 
Puteti verifica schimbarea culorii prin apelarea metodei descrie().
"""
# class Dreptunghi:
#     def __init__(self, lungime,latime,culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#     def descriere(self):
#         print(f" lungime={self.lungime},\n latime={self.latime}, \n culoare={self.culoare}")
#     def aria(self):
#         return self.lungime*self.latime
#     def perimetru(self):
#         return 2*(self.lungime+self.latime)
#     def schimba_culoarea(self,noua_culoare):
#         self.culoare=noua_culoare


# class Angajat:
#     def __init__(self, nume, prenume,salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#     def descriere(self):
#         print(f"Nume:{self.nume}\nPrenume:{self.prenume}\nSalariu:{self.salariu} lei")
#     def nume_complet(self):
#         print(f"Nume complet:{self.nume} {self.prenume}")
#     def salariu_lunar(self):
#         print(f"Salariul lunar: {self.salariu} lei")
#     def salariul_anual(self):
#         anual=self.salariu*12
#         print( f"Salariul anual: {anual} lei")
#     def marire_salariu(self,procent):
#         marire=self.salariu*procent/100
#         print( f"Marire: {marire} lei" )

"""4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode: ● afisare_sold() - Titularul x are în contul y suma de n lei ● debitare_cont(suma) 
● creditare_cont(suma)
"""

# class Cont:
#     def __init__(self, iban, titular_cont,sold):
#         self.iban=iban
#         self.titular_cont=titular_cont
#         self.sold=sold
#     def afisare_sold(self):
#         print(f"Titlarul {self.titular_cont} are in cont suma de {self.sold} lei")
#     def debitare_cont(self,suma):
#         self.sold-=suma
#     def cretitare_sold(self,suma):
#         self.sold+=suma

"""
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
"""
# from prettytable import PrettyTable
# from datetime import date
#
# class Factura:
#     seria = 3726948142
#     def __init__(self, numar,nume_produs,cantitate,pret_buc):
#         self.numar= numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitatea(self,cantitate):
#         self.cantitate=cantitate
#     def schimbă_pretul (self,pret):
#         self.pret_buc=pret
#     def schimba_nume_produs(self,nume):
#         self.nume_produs=nume
#
#     def genereaza_factura(self):
#         x = PrettyTable()
#         today = date.today()
#         total=self.pret_buc*self.cantitate
#         print(f"Factura nr:{self.seria} data:{today}")
#         x.field_names = ["Nume Produs", "Cantitate", "Pret bucata", "Total"]
#         x.add_row( [self.nume_produs, self.cantitate, self.pret_buc, total ] )
#         print(x)

"""2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
"""
# class Masina:
#     marca="Ford"
#     model=None
#     viteza_maxima=None
#     viteza_actuala=0
#     culoare="gri"
#     culori_disponibile= {"rosu","galben","verde","albastru","alb","negru","gri"}
#     inmatriculata=False
#     def __init__(self, model, viteza_maxima):
#         self.model=model
#         self.viteza_maxima=viteza_maxima
#     def descriere(self):
#         print(f"Marca: {self.marca}\nModel: {self.model}\nViteza maxima: {self.viteza_maxima}\n"
#               f"Viteza actuala: {self.viteza_actuala}\nCuloare: {self.culoare}\nInmatriculata: {self.inmatriculata}\n")
#     def inmatriculate(self,inmatriculata):
#         self.inmatriculata=inmatriculata
#     def vopseste(self,culoare):
#         assert culoare in self.culori_disponibile,"Culoarea nu este disponibila"
#         self.culoare=culoare
#     def accelerează(self,viteza):
#         assert viteza>0,"The speed cannot be negative"
#         if viteza>self.viteza_maxima:
#             viteza=self.viteza_maxima
#         self.viteza_actuala+=viteza
#     def franeaza(self):
#         self.viteza_actuala=0
#
# masina=Masina("Focus",200)
# masina.descriere()
# masina.vopseste("albastru")
# masina.descriere()
# masina.accelerează(30)
# masina.descriere()
# masina.franeaza()
# masina.descriere()

"""3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor

Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
"""
class Todo:
    todo={}
    def adauga_task(self,nume,descriere):
        # self.nume=nume
        # self.descriere=descriere
        self.todo[nume]=descriere

    def finalizeaza_task(self,nume_task):
        del self.todo[nume_task]
    def afiseaza_todo_list(self):
        print(self.todo)
    def afișează_detalii_suplimentare(self,nume_task):
        if nume_task not in self.todo.keys():
            intreaba=input("The task is not in your list.\nWould you like to add a new task?")
            if intreaba=="no":
                print("Ok, bye !!!")
            elif intreaba=="yes":
                nume=input("Add a name for the new task")
                descriere=input("Add the task's descripion")
                self.todo[nume] = descriere
                print( f"{nume}:{descriere } has been added to your list")
            else:
                print("Aswer with yes or no")


todo=Todo()
todo.adauga_task("task1","codeaza un website")
todo.afiseaza_todo_list()
todo.finalizeaza_task("task1")
todo.afiseaza_todo_list()
todo.afișează_detalii_suplimentare("task2")
todo.afiseaza_todo_list()