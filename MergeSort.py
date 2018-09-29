def MergeSort(x):
    if len(x) < 2:
        return x
    result = []  # store the results
    mid = int(len(x) / 2)  # get the middle number. int(9/2)==4.  x = [12, 43, 67, 52, 88, 94, 29, 49, 60]
    a = MergeSort(x[:mid])  # divide the list:left = [12, 43, 67, 52],then [12,43]+[67,52], then [12],[43],[67].[52]
    print("a:", a)
    b = MergeSort(x[mid:])  # right = [88, 94, 29, 49, 60], then [88,94]+[29,49,60],then [88],[94],[29],[49],[60]
    print("b:", b)
    # stop
    while (len(a) > 0) and (len(b) > 0):  # Check list empty or not
        if a[0] > b[0]:  # if left > right
            result.append(b[0])  # add b[0] to result
            b.pop(0)  # remove b[0]
        else:
            result.append(a[0])  # 12<88. copy 88 to result
            a.pop(0)  # remove 12 from a
    result += a
    result += b
    print("Result:", result)
    return result


x = [12, 43, 67, 52, 88, 94, 29, 49, 60]
MergeSort(x)
