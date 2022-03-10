import literales as msg
import functions as f


def main():

    file = input(msg.MSG6)
    f_name = f.val_file(file)
    aux = f.check_file(f_name)
    if aux == 0:  # Printo la capçalera si el fitxer no existeix.
        f.add_dict(f_name, aux)
    else:
        f.add_dict(f_name, aux)


if __name__ == '__main__':
    main()