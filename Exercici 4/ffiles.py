import literales as msg
import nilib
import csv


def opcion():
    option = nilib.validate(msg.MSG4,1,3)
    if option == 1:
        return msg.INT1
    elif option == 2:
        return msg.INT2
    else:
        return msg.INT3


def cabecera():
    with open(msg.ROUTE + 'base.csv', 'a') as csvfile:
        writecsv = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writecsv.writerow(['ID', 'Name', 'Surname', 'Age', 'Interest'])


def introducir(id, name, surname, age, interest):
    with open(msg.ROUTE + 'base.csv', 'a') as csvfile:
        writecsv = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writecsv.writerow([id, name, surname, age, interest])
