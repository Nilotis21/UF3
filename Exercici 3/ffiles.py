import literales as msg
import nilib


def mod_file(f):
    f = open(f, "w")
    x = nilib.validate(msg.MSG3, 1, None)
    for i in range(x):
        txt = input(msg.MSG4 + str(i + 1) + ": ")
        f.write(txt + "\n")
    f.close()


def only_create(f):
    f = open(f, "w")
    f.close()


def read_file(f_name):
    f = open(f_name, "r")
    print()
    print(f.read())
    f.close()

