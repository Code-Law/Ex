for i in range(100000, 999999):
    if sorted(str(i)) == sorted(str(2 * i)) == sorted(str(3 * i)) == sorted(str(4 * i)) == sorted(str(5 * i)) == sorted(
            str(6 * i)):
        print(i)

# for haha in range(100000, 1000000):
#     hia = (str(haha))
#     if str(haha) == str(2 * haha) == str(3 * haha) == str(4 * haha) == str(5 * haha) == str(6 * haha):
#         print(''.join(sorted(hia)))
#         break
