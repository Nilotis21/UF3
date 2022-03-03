import csv
import literales as msg

def prn_header():
    with open('files/books.csv', 'a+', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['Data', 'Nom', 'Localització', 'Espècie', 'Mida', 'Característiques']
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writeCSV.writeheader()


def insert_log():
    aux = 1
    while aux == 1:
        bio = dict()
        bio['Data'] = input(msg.MSG1)
        bio['Nom'] = input(msg.MSG2)
        bio['Localització'] = input(msg.MSG3)
        bio['Espècie'] = input(msg.MSG4)
        bio['Mida'] = input(msg.MSG5)
        bio['Característiques'] = input(msg.MSG6)
        aux = int(input(msg.AUX))
        return bio


def add_dict():
    book = insert_log()
    with open('files/bio.csv', 'a+', encoding='utf-8', newline='\n') as csvfile:
        fieldnames = ['Data', 'Nom', 'Localització', 'Espècie', 'Mida', 'Característiques']
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
        try:
            writeCSV.writerow(book)
        except:
            print("No s'ha pogut inserir el registre.")
        else:
            print("El registre s'ha inserit correctament.")


def rd_dict(f_name):
    with open(f_name, encoding="utf8") as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter=',')
        line_count = 0
        print("La capçalera és: \n", end="")
        for i in range(len(readCSV.fieldnames)):
            if i < (len(readCSV.fieldnames) - 1):
                print(readCSV.fieldnames[i], end=", ")
            else:
                print(readCSV.fieldnames[i], end="")
        print()
        for row in readCSV:
            print(f'{row["Data"]},{row["Nom"]},{row["Localització"]},{row["Espècie"]},{row["Mida"]},{row["Característiques"]},;\n')
            line_count += 1
        print(f"S\'han llegit {line_count} lines.\n")