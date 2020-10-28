def validate_length(length):
    return 3 <= length <= 16


def validate_characters(name):
    allowed_chars = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-')
    return not set(name).issubset(allowed_chars)


user_names = input().split(', ')
for user in user_names:
    if validate_length(len(user)) and validate_characters(user) == 0:
        print(user)

