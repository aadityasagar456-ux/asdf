list = [1, 2, 3, 4, 5]

for i in range(0,10):
    p = int(input("enter a number:"))
    list.append(p)

    list2 = []

    for i in list:
        if i not in list2:
            list2.append(i)

print("list after removing duplicates:")
print(list2)
