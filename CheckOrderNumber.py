print("Input Order# (Format eg.HaP132, haP123, hap23a, HAP283")
print("\n")
while True:
    global orderNumber  # initialisation of global variable to store order number and to use outside of this Function
    orderNumber = str(input("Input Order number: "))
    a = orderNumber[0:2].isalpha()  # sets 1st to 3rd character to be any case
    b = orderNumber[3:5].isdigit()  # sets 4th to 6th character to single-digit integers
    if a == False or b == False:
        print("Wrong format.")
    else:
        break
