# poezie="Ana are mere si este vesela pentru ca este miercuri"
#
# print(poezie[0:len(poezie)])
# print(poezie[:])
# print(poezie[::])
#
# print(poezie[0:len(poezie):2])
# print(poezie[-3:])
# print(poezie[::-1])
#
# print(poezie.split(sep=" "))
#
#
# # print(poezie.replace("A","m"))
# # print(poezie.replace("Ana","Maria"))
#
# # print(poezie.upper())
# # print(poezie.upper().replace("A", "m"))
#
# print(poezie.index("A"))
# # print(poezie.find("x"))
# # print(poezie.index("x"))
#
# # metoda isnumeric(), metoda count(), metoda capitalize()
# # numeric="1234"
# # print(poezie.isnumeric())
# # print(numeric.isnumeric())
# #
# # print(poezie.count("a"))
# # print(poezie.count("A"))
# #
# # print(poezie.capitalize())
#
# # """Operatorii
# # - De atribuire
# # - Aritmetici
# # - De comparare
# # - Logici
# # """
# var1=7
# var2=2
# var1+=1
# print(id(var1))
# var1=var1-1
# print(id(var1))
# print(var1//var2)

# text=input("Scrie un text ").lower()
# if (text[0])==text[-1]:
#     print("este")
# else:
#     print("nu este")




# if x==y==z:
#     print("Triunghiul este echilateral")
# elif x==y or x==z or y==z:
#     print( "Triunghiul este isoscel" )
# else:
#     print( "Triunghiul este oarecare" )


# nr='0123456789'
# print(nr[::2])
# print(nr[1::2])

from random import randint
comp_choice=randint(1,6)
your_choice=int(input("Chiceste zarul "))
if comp_choice==your_choice:
    print(f" Ai ghicit. Felicitari! Ai ales {your_choice} si zarul a fost {comp_choice}")
elif comp_choice<your_choice:
    print(f"Ai pierdut. Ai ales un numar mai mare.Ai ales {your_choice} si zarul a fost {comp_choice}")
else:
    print( f"Ai pierdut. Ai ales un numar mai mic.Ai ales {your_choice} si zarul a fost {comp_choice}" )