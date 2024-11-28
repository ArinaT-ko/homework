immutable_var = 1, 'list', True, 15
print('Immutable tuple: ', immutable_var)
#immutable_var[0] = 1 - невозможно изменить, тау как кортеж - неизменяемый!!

mutable_list = [13, 24, 17, 18]
mutable_list[0] = 218
mutable_list.append(185)
print('Mutable list: ', mutable_list)