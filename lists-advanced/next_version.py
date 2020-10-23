version = input().split('.')
version_number = int(''.join(version))
next_version = '.'.join(str(version_number + 1))
print(next_version)