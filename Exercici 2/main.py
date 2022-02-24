import literales as msg
import ffiles
import nilib


def main():
    text = input(msg.MSG1)
    while len(text) < 0 or len(text) > 100:
        text = input(msg.MSG1)
    ffiles.create_file(msg.ROUTE + "text.txt", text)


if __name__ == "__main__":
    main()
