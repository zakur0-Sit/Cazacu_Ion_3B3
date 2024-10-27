def cmmdc(nr1, nr2):
    while nr1 != nr2:
        if nr1 < nr2:
            nr2 -= nr1
        else:
            nr1 -= nr2
    return nr1

print(cmmdc(24, 6))
print(cmmdc(155, 15))