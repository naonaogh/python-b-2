nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
new = [z for i in nice_list for j in i for z in j ]
print('Ответ:',new)
