import csv


def prn_header():
    with open('files/books.csv', 'a+', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['isbn', 'title', 'author', 'editorial', 'pub_date']
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writeCSV.writeheader()


def add_dict(book):
    with open('files/books.csv', 'a+', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['isbn', 'title', 'author', 'editorial', 'pub_date']
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
        try:
            writeCSV.writerow(book)
        except:
            print("No s'ha pogut inserir el registre.")
        else:
            print("El registre s'ha inserit correctament.")
