# ex1:
# my_list=[
#     [1,"test1"],
#     [2,"test2",3,"test3"],
#     [34,"test4"],
#     [5]
# ]
# for i in range(0,len(my_list)):
#     for j in range (len(my_list[i])):
#         print(f"Valoarea curentaa elementului din lista de pe pozitia [{i}][{j}] este {my_list[i][j]}")

# cauta in list o valoare si inlocuieste-o cu alta valoare

# lista2=["gutui","prune","mere", "pere"]
# for i in range(len(lista2)):
#     print(lista2[i])
#     if lista2[i]=="gutui":
#         lista2[i]="caise"
# print(lista2)

# culorile_disponibile=["rosu", "albastru","roz", "verde", "galben", "violet", "magenta", "maro"]
# culori_nepotrivite=["galben","albastru","maro"]
#
# for culoare in range(len(culorile_disponibile)):
#     if culorile_disponibile[culoare] in culori_nepotrivite:
#         break
#     print(f"Va recomandam culoarea {culorile_disponibile[culoare]}")

# for each
# parcurgem lista si stergem daca intalnim soarece

# animale=["cal", "pisica", "caine", "magar","soarece","oaie"]
# for nr_animal in range(len(animale)-1):
#     if animale[nr_animal]=="soarece":
#         animale.pop(nr_animal)
# print(animale)

# for animal in animale:
#     if animal=="soarece":
#         animale.remove(animal)
# print(animale)

# printam nr pana la 5 cu for
# for i in range(6):
#     print(i)
# else:
#     print("am terminat")

# i=0
# while i<=5:
#     print(i)
#     i+=1
# else:
#     print("am terminat")

# FUNCTII


# def suma(a,b):
#     sum=a+b
#     print(f"Suma celor 2 nr este: {sum}")
#     return sum
# x=suma(2,4)
# print(x)

# Functii cu nr indefinit de parametrii

def calculeaza_pretul(*nr):
    pret=0
    for element in nr:
        pret=pret+element
    return pret

print(calculeaza_pretul(2,6,7))
print(calculeaza_pretul(1,3))
print(calculeaza_pretul(2,6,7,8,5,6,4))
print(calculeaza_pretul("casa","caine"))