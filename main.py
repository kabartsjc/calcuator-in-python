import awm

while True:
    ch = int(input(
    "Please enter progress\n"
    " 1-Addiction\n"
    " 2-Extraction\n"
    " 3-Division\n"
    " 4-Multiply\n"
    " 5-Powered\n"
    " 6-Square\n"
    " 7-Factorial\n"
    " Choosing:"
))

    if ch == 1:
        awm.add()
    elif ch == 2:
        awm.ext()
    elif ch == 3:
        awm.div()
    elif ch == 4:
        awm.multiply()
    elif ch == 5:
        awm.pov()
    elif ch == 6:
        awm.sqrt()
    elif ch == 7:
        awm.fac()
    else:
        break
