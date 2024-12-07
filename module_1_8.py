# Работа со словарями:

my_dict = {'Kira': 1920, 'Mark': 1978, 'Angela': 1999}

print('Dict: ', my_dict)

print('Existing value:', my_dict.get('Kira'))
print('Not existing value:', my_dict.get('Mari'))
my_dict.update({'Alex':1978,
               'Lina': 1923})
del_ = my_dict.pop('Mark')
print('Deleted value:', del_)

print('Modified dictionary:', my_dict)
print('')

# Работа с множествами:

my_set = {111, 111, 111, 1111, True, 'Oki'}
print('Set:', my_set)

my_set.add(314)
my_set.add(315)

my_set.remove(1111)

print('Modified set:', my_set)




