import ffiles as f
import literales as msg


def main():
    rep = 1
    f.cabecera()

    while rep == 1:
        name = input(msg.MSG1).capitalize()
        surname = input(msg.MSG2).capitalize()
        age = int(input(msg.MSG3))
        interest = f.opcion()
        id = (name[:2].upper() + "-" + surname[-2:].upper() + "-" + str(age))

        f.introducir(id, name, surname, age, interest)

        rep = int(input(msg.MSG5))


if __name__ == '__main__':
    main()