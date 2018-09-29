# 50 pieces of cash.
# How many combination.

# a = 0  # RMB 1 Count
# b = 0  # RMB 2 Count
# c = 0  # RMB 5 Count
# cc = 0  # Count
# for a in range(0, 51):
#     for b in range(0, 26):
#         for c in range(0, 11):
#             if (a + 2 * b + 5 * c) == 50:
#                 cc = cc + 1
# print(cc)

# $50 in all.
# How many combination?
a = 0  # RMB 1 Count
b = 0  # RMB 2 Count
c = 0  # RMB 5 Count
s = []
cc = 0  # value
for a in range(0, 51):
    for b in range(0, 51):
        for c in range(0, 51):
            cc = a + 2 * b + 5 * c
            if cc not in s:
                s.append(cc)
print(len(s))
