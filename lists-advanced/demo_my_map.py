def my_map(function, items):
    new_items = []

    for item in items:
        new_item = function(item)
        new_items.append(new_item)

    return new_items


strings = ['1', '2', '3', '4', '5']

my_map_result = my_map(lambda string: string + 'hello', strings)
map_result = list(map(lambda string: string + 'hello', strings))

print(strings)
print(my_map_result)
print(map_result)