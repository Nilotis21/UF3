def validate(msg, ini, fin):
    if fin is None:
        num = int(input(msg))
        while num < ini:
            num = int(input(msg))
    elif ini is None:
        num = int(input(msg))
        while num > fin:
            num = int(input(msg))
    elif ini is not None and fin is not None:
        num = int(input(msg))
        while num < ini or num > fin:
            num = int(input(msg))
    else:
        num = int(input(msg))
    return num

