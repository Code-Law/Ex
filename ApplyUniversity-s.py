password1 = "1234"
password = input("input password:")
counter = 0
while password != password1:
    counter = counter + 1
    if counter == 1:
        password = input("error,please input the password again,you have two more tries:")
    if counter == 2:
        password = input("error,please input the password again,you have one more tries:")
    if counter == 3:
        password = input("error,please contact service department")
        break


def UK():
    competition1 = ["1", "2", "3", "4"]
    competition = input("input the number of competitions you have entered:")
    if competition == "1" or competition == "2":
        print("Too low. Read admission requirements below:")
    if competition == "3":
        print("You may be considered if you have three A*. Read admission information below:")
        exit()

    if competition == "4":
        print("You may be considered if you have two A*s and an A.read admission requirement below:")
    while competition not in competition1:
        competition = input("error please input the number of competition again")


def USA():
    GPA1 = ["1", "2", "3", "4"]
    GPA = input("please input your GPA:")
    while GPA not in GPA1:
        GPA = input("error, please input your GPA again:")
        if GPA == "1" or GPA == "2":
            print("Too low. Read admission requirements below:")
            break
        if GPA == "3":
            print(
                "you may be considered if you participated in at least 3 international competitions,did at least two relevant community services that lasted for at least 150 hours,read admission requirement below:")
        if GPA == "4":
            print("you may be considered if you participated in at least 4 international competitions, attended an international field trip, participate in two or more community service projects that lasted for at least 100 hours,read admission requirements below:")


while password == password1:
    country1 = ["UK", "uk", "USA", "usa", "HK", "hk"]
    country = input("please input the country you want to go:")
    while country not in country1:
        country = input("error,please input the country you want to go again:")
    if country.upper() == "UK" or country.upper() == "HK":
        UK()
    if country.upper() == "USA":
        USA()
    # break
