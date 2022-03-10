import csv
import literales as msg
import nilib


def insert_log():  # Funcio que ompleix el diccionari i el retorna / ¡¡¡ Vigila amb les claus !!!
    log = dict()
    log['ID'] = input(msg.MSG1)
    log['Grupo/Cantante'] = input(msg.MSG2).capitalize()
    log['Canción'] = input(msg.MSG3)
    day = nilib.validate(msg.DD, 1, 31)
    # month = nilib.val_month(nilib.validate(msg.MM, 1, 12))
    month = nilib.validate(msg.MM, 1, 12)
    year = nilib.validate(msg.YYYY, 1970, None)
    log['Fecha'] = str(day) + '/' + str(month) + '/' + str(year)
    log['Views'] = input(msg.MSG5)
    return log


def add_dict(f_name, head):  # Funció que introdueix registres desde el diccionari, tantes vegades com es vulgui.
    aux = 1
    try:
        with open(f_name, 'a+', encoding='utf-8', newline='\n') as csvfile:
            fieldnames = ['ID', 'Grupo/Cantante', 'Canción', 'Fecha', 'Views']
            writecsv = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if head == 0:
                writecsv.writeheader()
            while aux == 1:
                log = insert_log()
                writecsv.writerow(log)
                aux = nilib.validate(msg.AUX, 0, 1)
    except:
        print(msg.MSG7)
    else:
        print(msg.MSG8)


def rd_dict(f_name):  # Funció que printar el csv i el nombre de registres.
    with open(f_name, encoding="utf8") as csvfile:
        readcsv = csv.DictReader(csvfile, delimiter=',')  # Ojo con el delimitador
        line_count = 0
        # sumatorio = 0
        # Printar la capçalera per consola
        '''for i in range(len(readcsv.fieldnames)):
            if i < (len(readcsv.fieldnames) - 1):
                print(readcsv.fieldnames[i], end=", ")
            else:
                print(readcsv.fieldnames[i], end="")
        print()'''
        for row in readcsv:
            print(f'{row["ID"]},{row["Grupo/Cantante"]},{row["Canción"]},{row["Fecha"]},{row["Views"]};\n')
            line_count = line_count + 1

        print(f"N\'hi ha {line_count} registres.")
        # print(f"N\'hi ha {sumatorio} dones.\n")


def check_file(file):  # Verifico si el fitxer existeix
    try:
        with open(file, 'r'):
            return 1
    except FileNotFoundError:
        return 0


def val_file(f_name):  # Creo fitxer csv tingui o no la extensió
    if msg.EXT2 in f_name[:4]:
        return msg.ROUTE + f_name
    else:
        return msg.ROUTE + f_name + msg.EXT2


def get_info(f_name):  # Funció que selecciona columnes i compta registres
    line_count = 0
    sumatorio = 0
    with open(f_name, encoding="utf8") as csvfile:
        readcsv = csv.DictReader(csvfile)
        for row in readcsv:
            sumatorio += int(row['key'])
            line_count += 1
        print(f'El document conté {line_count} projecte i el sumatori és {sumatorio}')
