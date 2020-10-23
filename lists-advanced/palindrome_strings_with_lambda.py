words = input().split()
searched_palindrome = input()

palindromes = list(filter(lambda word: word == word[::-1], words))
count = palindromes.count(searched_palindrome)

print(palindromes)
print(f'Found palindrome {count} times')