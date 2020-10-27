my_dict = {1: 'apple', 2: 'banana'}
my_dict.clear()

my_dict_second = {'name': 'Beni', 'age': 33}
my_dict_third = my_dict_second.copy()
print(my_dict_third)

item = my_dict_second.pop('age')
print(my_dict_second)
print(item)

print(my_dict_third.popitem())