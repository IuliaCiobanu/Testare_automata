
# def calculeaza(a,b):
#     sum=a+b
#     return sum
# print(calculeaza(2,3))

# def parimpar(a):
#     if a%2==0:
#         return True
#     else:
#         return False
# print(parimpar(2))

# def nr_litere(nume,prenume,nume_mijloc):
#    total_litere=len(nume)+len(prenume)+len(nume_mijloc)
#    return total_litere
# print(nr_litere("Ciobanu","Iulia","Georgiana"))

# def arie_dreptunghi(lungime,latime):
#     aria=lungime*latime
#     return aria
# print(arie_dreptunghi(4,6))

# def arie_cerc(raza):
#     arie=3.14*(raza**2)
#     return arie
# print(arie_cerc(2))

# cuvant="spanzuratoarea"
# def verifica(litera):
#     if litera in cuvant:
#         return True
#     else:
#         return False
# print(verifica("w"))

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

# cap=0
# low=0
# def vezi_upper(cuvant):
#     global cap
#     global low
#     for litera in cuvant:
#         if litera.isupper():
#             cap= cap+1
#         else:
#             low=low+1
#     print(f"Cuvantul are {cap} litere mari si {low} litere mici")
# vezi_upper("ACAsa")

# lista=[-2,-1,0,4,5,8]
# lista1=[]
# def lista_pozitiva(lista):
#     for nr in lista:
#         if nr>=0:
#             lista1.append(nr)
#     return lista1
# print(lista_pozitiva(lista))

# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

# def compara_nr(x,y):
#     if x==y:
#         print("Numerele sunt egale")
#     elif x>y:
#         print("Primul număr x este mai mare decat al doilea nr y")
#     else:
#         print("Al doilea nr y este mai mare decat primul nr x")
#
# compara_nr(4,8)

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False


# def primeste_set(nr,set):
#     if nr in set:
#         print("Printeaza ‘nu am adaugat numărul în set. Acesta există deja’")
#         return False
#     else:
#         set.add(nr)
#         print(set)
#         print("Printeaza ‘am adaugat numărul nou în set’")
#         return True
# primeste_set(1,{2,3,4,5})
# lunile_anului={"ianuarie":31,"februarie":28,"martie":31,"aprilie":30,"mai":31,"iunie":30,"iulie":31,
#                "august":31,"septembri":30,"octombrie":31,"noiembrie":30,"decembrie":31}
# def zile_in_luna(luna):
#     return lunile_anului[luna]
# print(zile_in_luna("mai"))

# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
# În final vei putea face: a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

# def calculator(x,y):
#     a=x+y
#     b=x-y
#     c=x*y
#     d=x/y
#     return a,b,c,d
# a,b,c,d=calculator(2,3)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

# dictionar={}
# def nr_in_lista(lista):
#     for nr in range(10):
#         x=lista.count(nr)
#         dictionar[nr]=x
#     return dictionar
# print(nr_in_lista([3,3,5,4]))

# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

# def nr_maxim(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(nr_maxim(1,2,3))

"""5. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)"""

# x = 0
# def calc_suma(nr):
#     global x
#     for a in range(0,nr+1):
#         x=x+a
#     return x
# print(calc_suma(10))

# def nr_comune(a,b):
#     new_list=[]
#     for nr in a:
#         if nr in b:
#             new_list.append(nr)
#     return new_list
# print(nr_comune([2,3,4,5,6,7],[1,2,3,4,5]))

# pret_produs=200
# def aplica_reducere(x):
#     global pret_produs
#     if x<100:
#         reducere=(x*pret_produs)/100
#         pret_produs=pret_produs-reducere
#         print(pret_produs)
# aplica_reducere(10)

import datetime
current_time = datetime.datetime.now()
print(current_time)

