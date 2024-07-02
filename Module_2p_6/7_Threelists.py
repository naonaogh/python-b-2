array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

def itsection_using_sets(array_1, array_2, array_3):
    intersection = set(array_1).intersection(array_2)
    return sorted(intersection)

def itsection_without_sets(array_1, array_2, array_3):
    new_arr = array_1 + array_2 + array_3
    new_new_arr = []
    for i in range(len(new_arr)):
        for j in range(i+1, len(new_arr)):
            if (new_arr[i] == new_arr[j]) and (new_arr[i] not in new_new_arr):
                new_new_arr.append(new_arr[i])

    return new_new_arr

#найти элементы из первого списка, которых нет во втором и третьем списках.
def difference_using_set(array_1, array_2, array_3):
    diff = [x for x in array_1 if x not in array_2 and x not in array_3]
    return diff

def difference_without_set(array_1, array_2, array_3):
    new_arr = []
    for i in range(len(array_1)):
        for j in range(0, len(array_2)):
            for k in range(0, len(array_3)):
                if (array_1[i] != array_2[j]) and (array_1[i] != array_3[k]) and (array_1[i] not in array_2) and (array_1[i] not in array_3) and (array_1[i] not in new_arr):
                    new_arr.append(array_1[i])

    return new_arr


print(itsection_using_sets(array_1, array_2, array_3))
print(itsection_without_sets(array_1, array_2, array_3))
print(difference_using_set(array_1, array_2, array_3))
print(difference_without_set(array_1, array_2, array_3))
