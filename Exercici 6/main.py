import csv
import literales as msg
import functions as f


def main():

    aux = 1
    f.prn_header()
    while aux == 1:
        book = dict()
        book['isbn'] = input(msg.MSG1)
        book['title'] = input(msg.MSG2)
        book['author'] = input(msg.MSG3)
        book['editorial'] = input(msg.MSG4)
        book['pub_date'] = input(msg.MSG5)
        f.add_dict(book)
        aux = int(input(msg.AUX))


if __name__ == '__main__':
    main()
