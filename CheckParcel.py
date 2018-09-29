A_length = []
A_width = []
A_height = []
A_weight = []

R_length = []
R_width = []
R_height = []
R_weight = []

A_Sum_lwh = []

ts = 0
tp = 0

i = 0
j = 0
k = 0
p = 0
a = 0
r = 0
n = 0
length = 0
width = 0
height = 0
weight = 0

n = int(input("How many parcels would you like to input?"))
for i in range(n):
    length = int(input("input length:"))
    width = int(input("input width:"))
    height = int(input("input height:"))
    weight = int(input("input height:"))
    if (length >= 80) or (width >= 80) or (height >= 80) or ((length + width + height) > 200) or (
            (weight > 1) and (weight > 10)):
        print("Reject!")
        R_length.append(length)
        R_width.append(width)
        R_height.append(height)
        R_weight.append(weight)
        r = r + 1
    else:
        print("Accept!")
        A_length.append(length)
        A_width.append(width)
        A_height.append(height)
        A_weight.append(weight)
        a = a + 1

print("===================")
print("Accept List:")
for j in range(a):
    print(A_length[j], A_width[j], A_height[j], A_weight[j])
print("===================")
print("Reject List:")
for j in range(r):
    print(R_length[j], R_width[j], R_height[j], R_weight[j])

for k in range(a):
    s = s + A_weight[k]
print(s)  # Total Weight

# Calculate Total Weight
for p in range(a):
    if (A_weight[p] >= 1) and (A_weight[p] <= 5):
        tp = tp + 10
    else:
        tp = 10 + ((A_weight[p] - 5) / 0.1) * 0.1
print(tp)
