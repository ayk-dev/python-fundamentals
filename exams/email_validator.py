email = input()

while True:
    line = input()
    if line == 'Complete':
        break

    args = line.split()
    command = args[0]
    if command == 'Make':
        result = ''
        if args[1] == 'Upper':
            for ch in email:
                if ch.isalpha():
                    ch = ch.upper()
                result += ch
            email = result
            print(email)

        else:
            for ch in email:
                if ch.isalpha():
                    ch = ch.lower()
                result += ch
            email = result
            print(email)

    elif command == 'GetDomain':
        count = int(args[1])
        print(email[-count:])

    elif command == 'GetUsername':
        if '@' not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
            continue
        username = ''
        for ch in email:
            if ch == '@':
                break
            username += ch
        print(username)

    elif command == 'Replace':
        replace = args[1]
        while replace in email:
            email = email.replace(replace, '-')
        print(email)

    elif command == 'Encrypt':
        encrypted = []
        for ch in email:
            encrypted.append(str(ord(ch)))
        print(' '.join(encrypted))
