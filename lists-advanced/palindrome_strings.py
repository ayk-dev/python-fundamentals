def is_palindrome(word):
    return word == word[::-1]

is_it_palindro

words = input().split()
searched_palindrome = input()

palindromes = [string for string in words if is_palindrome(string)]
counter = palindromes.count(searched_palindrome)

print(palindromes)
print(f'Found palindrome {counter} times')