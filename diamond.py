
def dia():
    b=0
    print("                        *")
    for n in range(20,1,-2):
        b=b+4
        print(" " * n, "*"," " * b, "*")
    for j in range(1, 20, 2):
        print(" " * j, "*"," " * b, "*")
        b = b -4
    print("                       *")
dia()