def Logic_Gate():
    A = input("Please input A:")
    while A.isdecimal() == False:
        A = input("Error Type! Please input A:")
    B = input("Please input B:")
    while B.isdecimal() == False:
        B = input("Error Type! Please input B:")
    C = input("Please input C:")
    while A.isdecimal() == False:
        C = input("Error Type! Please input C:")
    # NOT
    print(not A)
    print(not B)
    print(not C)
    # AND
    print(A and B and C)
    # OR
    print(A or B or C)
    # NOR
    print(not (A or B or C))
    # NAND
    print(not (A and B and C))
    # XOR
    print(bool(A) != bool(B) != bool(C))


while True:
    Logic_Gate()
