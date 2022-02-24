def create_file(f, text):
    f = open(f, "w")
    f.write(text)
    f.close()