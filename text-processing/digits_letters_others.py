data = input()
print(''.join([ch for ch in data if ch.isdigit()]))
print(''.join([ch for ch in data if ch.isalpha()]))
print(''.join([ch for ch in data if not ch.isalnum()]))