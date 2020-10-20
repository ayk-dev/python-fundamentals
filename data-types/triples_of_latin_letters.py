n = int(input())

start_range = 97
end_range = start_range + n

for a in range(start_range, end_range):
    for b in range(start_range, end_range):
        for c in range(start_range, end_range):
            print(chr(a) + chr(b) + chr(c))