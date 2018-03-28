import math
from time import clock

def decomposition_binaire(nombre):
    #definitions de variables
    string = ''
    plus_grande_puissance = math.floor(math.log(nombre, 2))
    nombre_en_binaire = [0] * (int(plus_grande_puissance+1))
    nombre_en_binaire[0] = 1
    reste = nombre - 2 ** plus_grande_puissance
    n = plus_grande_puissance
    #transformation du nombre en binaire (dans une liste)
    while reste > 0:
        n -= 1
        if  reste >= 2 ** n:
            nombre_en_binaire[plus_grande_puissance - n] = 1
            reste -= 2 ** n
    for i in range(len(nombre_en_binaire)): #conversion du nombre en une string (inutilisé dans ce programme)
        string += str(nombre_en_binaire[i])
    nombre_en_binaire_format_int = int(string) #conversion du nombre en un entier (inutilisé dans ce programme)
    return nombre_en_binaire
def fast_modular_exponentiation(nombre, exposant, modulo):
    #definitions des variables et des listes
    reste_des_puissances_de_2 = []
    reste_dans_div_eucli_de_nombre_exposant_par_modulo = 1
    exposant_en_binaire = decomposition_binaire(exposant)
    reste_des_puissances_de_2.append(nombre % modulo)
    for i in range(1, len(exposant_en_binaire)):
        reste_des_puissances_de_2.append((reste_des_puissances_de_2[i-1])**2 % modulo)
    reste_des_puissances_de_2.reverse()

    #processus de l'exponentiation modulaire rapide
    for i in range(len(exposant_en_binaire)):
        if exposant_en_binaire[i] == 1:
            reste_dans_div_eucli_de_nombre_exposant_par_modulo = reste_dans_div_eucli_de_nombre_exposant_par_modulo * reste_des_puissances_de_2[i] % modulo

    return reste_dans_div_eucli_de_nombre_exposant_par_modulo


while True:
    print('Entrez successivement trois entiers naturels. Ce programme calcule le reste dans la division euclidienne de x^y par z.')
    nombre = int(input('Entrez la valeur de x soit le nombre que l\'on éleve à une puissance :'))
    exposant = int(input('Entrez maintenant la valeur de y, soit de l\'exposant :'))
    modulo = int(input('Entrez z, soit la valeur du modulo :'))
    debut = clock()
    print(fast_modular_exponentiation(nombre, exposant, modulo))
    fin = clock()
    duree = fin - debut
    tmp = input('Calcul effectué en ' + str(duree) + ' secondes.\nAppuyer sur "Entrer" pour continuer ...')