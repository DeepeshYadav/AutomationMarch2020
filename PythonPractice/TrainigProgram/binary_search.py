def binary_sear(alist, item):
    first = 0
    last = len(alist) -1
    found = False

    while first <= last and not found:
        pos =0
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            pos = midpoint
            found= True
        else:
            if item < alist[midpoint]:
                last = midpoint -1
            else:
                first = midpoint + 1

    return pos, found

alist = [1, 5, 6, 8, 9, 23, 56]
print(binary_sear(alist,9))