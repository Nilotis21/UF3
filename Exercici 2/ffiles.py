def create_file(f, text):
    f = open(f, "a")
    f.write(text + " ")
    f.close()