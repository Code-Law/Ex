# login
PasswordA = "Abc123"
count = 0
Country = ["UK", "USA", "USA"]
while count < 3:
    PasswordB = input("Please input password:")
    if PasswordA != PasswordB:
        print("Wrong! Please input password again:")
    else:
        print("Right! Now choose a country!")
        print("Please choose the country you want to study in:")
        School = input("UK,USA or HK:")
        while School not in Country:
            School = input("Error! Please input the country again:")
            if School == "UK" or School == "HK":
                UK()
            elif School == "USA":
                USA()
            
    count = count + 1
    if count == 3:
        print("Too many wrong inputs. Programme Terminal...")
        exit()

#  University Country Define
# def UK():
