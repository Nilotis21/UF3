import literales as msg
import ffiles
import nilib
'''Implementa un programa que mostri un menú amb les següents opcions:
crear un fitxer (demanant el nom del fitxer a l’usuari per teclat)
mostrar el contingut d’un fitxer per pantalla (demanant el nom del fitxer a l’usuari per teclat)
modificar el contingut d’un fitxer demanant el nom del fitxer a l’usuari per teclat)
'''


def main():
    x = nilib.validate(msg.MENU + "\n", 1, 4)
    match(x):
        case 1:
            f_name = input(msg.MSG1)
            ffiles.only_create(msg.ROUTE + f_name)
        case 2:
            f_name = input(msg.MSG2)
            ffiles.read_file(msg.ROUTE + f_name)
        case 3:
            f_name = input(msg.MSG2)
            ffiles.mod_file(msg.ROUTE + f_name)
        case _:
            print(msg.EXIT)





if __name__ == "__main__":
    main()
