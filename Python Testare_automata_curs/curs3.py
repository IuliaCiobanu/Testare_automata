# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina.lower()=="mercedes":
#         print(f"Am găsit mașina dorită de dvs")
#         break
#     else:
#         print( f"Nu am găsit mașina dorită de dvs" )



# i=0
# while i<len(masini)+1:
#     print( f"Masina mea preferata este {masini[i]}" )
#     i+=1



# for i in range(1,len(masini)-1):
#     masini[i]=masini[i].upper()
# else:
#     print( masini )


# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina.lower()=="trabant" or masina.lower()=="lăstun":
#         continue
#     print( f"S-ar putea sa va placa masina {masina}" )


# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# masini_vechi=[]
#
# for i in range(len(masini)):
#     if masini[i] in ['Lăstun', 'Trabant']:
#         masini_vechi.append(masini[i])
#         masini[i]="Tesla"
# print(masini)
# print(masini_vechi)


pret_masini = { 'Dacia': 6800, 'Lăstun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000 }
for Dacia in pret_masini:
     print("ok")
# for key,value in pret_masini.items():
#     if value<15000:
#         print(f"Pentru un buget de sub 15000 euro puteți alege mașină {key}")


# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for i in range(len(numere)):
#     if numere[i] >0:
#         numere[i] = -numere[i]
# print(numere)

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for nr in alte_numere:
#     if nr%2==0 and nr>0:
#         numere_pare.append(nr)
#         numere_pozitive.append(nr)
#     elif nr%2==0 and nr<0:
#         numere_pare.append(nr)
#         numere_negative.append(nr)
#     elif nr % 2 != 0 and nr > 0:
#         numere_impare.append(nr)
#         numere_pozitive.append(nr)
#     else:
#         numere_impare.append( nr )
#         numere_negative.append( nr )
# print(f"negative: {numere_negative}")
# print( f"pozitive:{numere_pozitive}")
# print( f"impare:{numere_impare}")
# print(f"pare:{numere_pare}")





