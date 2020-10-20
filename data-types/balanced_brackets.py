n = int(input())
my_list = []
is_balanced = True
old_line = ''

for i in range(n):
    line = input()
    if line == '(' and old_line == '(':
        is_balanced = False
    my_list.append(line)
    old_line = line

if my_list.count('(') == my_list.count(')') and is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')


