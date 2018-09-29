def circle_sum(n):
    if n == 1:
        return 1
    else:
        return 16 * n * n - 28 * n + 16

# top_right = (2 * n - 1) ** 2
# top_left = (2 * n - 1) ** 2 - ((2 * n - 1) - 1)
# bottom_left = (2 * n - 1) ** 2 - 2 * ((2 * n - 1) - 1)
# bottom_right = (2 * n - 1) ** 2 - 3 * ((2 * n - 1) - 1)

final_sum = 0
p = int(input("Please input p:"))
for i in range(1, p + 1):
    final_sum = final_sum + circle_sum(i)
print(final_sum)
