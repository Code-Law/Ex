# -*- coding:utf-8 -*-
# Generate Random Password
import random
import string
ss = '#@$%^&*()_+=,.?!'
# print(ss)
# python3:string.ascii_letters

def gen_password(length):
    chars = ss + string.ascii_letters + string.digits
    # with duplicated
    return ''.join([random.choice(chars) for i in range(length)])
    # return ''.join(random.sample(chars, 15))#no duplicated

if __name__ == "__main__":
    # Generate 10 Random Password
    for i in range(10):
        # Password Length
        print (gen_password(24))
