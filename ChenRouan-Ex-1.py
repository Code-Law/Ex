# Write a program to generate a password for user with functions below:
# User can choose the length(8-32).
# User can choose data type(letter,digit,punctuation), or mixed.
# Calculate how many times Computer can guess right at worst.
# Create an algorithm to estimate the complexity and show why.
# Output the complexity of the password generated by user.
input_length = int(input('please input the length of your password(8-32):'))
input_type = str(input('please choose one type(letter,digit,punctuation,mixed):'))
final_password = []


def choosetype(length, type):
    password = []
    import random
    if type == 'digit':
        complexity = 10 ** length
        for time in range(0, length):
            password.append(str(random.randint(0, 9)))

    elif type == 'letter':
        complexity = 52 ** length
        for time in range(0, length):
            password.append(str(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')))

    elif type == 'punctuation':
        complexity = 13 ** length
        for time in range(0, length):
            password.append(str(random.choice('@#$%^&*(),.?`')))

    elif type == 'mixed':
        complexity = 55 ** length
        for time in range(0, length):
            password.append(str(random.choice( \
                '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ！@#¥%……&*,.?`')))

    print(''.join(password))
    print(complexity)
    if complexity < 20 ** 20:
        print('Complexity:Simple.')
    elif complexity >= 20 ** 20 and complexity <= 25 * 25:
        print('Complexity:Median.')
    else:
        print('Complexity:Hard.')


if input_length in range(8, 33):
    choosetype(input_length, input_type)
else:
    print('out of range,please try again')
