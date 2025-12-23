def kaprekarNumbers(p, q):
    total = ""
    for i in range(p, q+1):
        if i == 1:
            total += "1 "
            continue
        if i < 9:
            continue
        j = i**2
        j = str(j)
        list_i = list(map(int,[j[:(len(j)//2)], j[(len(j)//2):]]))
        if sum(list_i) == i:
            total += str(i) + " "
    print(total) if total else print("INVALID RANGE")
print(kaprekarNumbers(2, 4))
