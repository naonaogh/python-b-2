list1 = [1, 3, 5, 10]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = []
list1.extend(list2)
new = set(list1)
list3.extend(new)
print(list3)

