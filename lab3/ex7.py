def is_palindrome(arr):
    palindrome_count = 0
    max_palindrome = -1
    for i in arr:
        if str(i) == str(i)[::-1]:
            palindrome_count += 1
            if i > max_palindrome:
                max_palindrome = i
    if max_palindrome == -1:
        max_palindrome = None
    return palindrome_count, max_palindrome

print(is_palindrome([121, 123, 454, 789, 22, 30]))
print(is_palindrome([123, 456, 789, 2345, 6789, 890, 4321]))