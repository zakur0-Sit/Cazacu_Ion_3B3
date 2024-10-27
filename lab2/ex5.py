def palindrome(number):
    return str(number) == str(number)[::-1]

print(palindrome(1234))
print(palindrome(1234321))
print(palindrome(1234554321))