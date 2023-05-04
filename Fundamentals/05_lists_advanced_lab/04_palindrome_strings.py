# words = input().split()
# looking_for = input()
# all_palindromes = [word for word in words if word == word[::-1]]
# print(all_palindromes)
# print(f"Found palindrome {all_palindromes.count(looking_for)} times")

strings = input().split(" ")
searched_palindrome = input()
palindromes = []
for word in strings:
    if word == "".join(reversed(word)):
        palindromes.append(word)
print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")
