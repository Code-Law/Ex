x = input("input red or green:")
print(x.lower() != 'red' or x.lower() != 'green')
while (x.lower() != 'red' or x.lower() != 'green') == True:
    x = input("Sorry!input red or green:")
print("OK")
