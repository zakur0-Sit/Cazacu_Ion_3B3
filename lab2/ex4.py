def camel_to_lower(string):
    word = string[0]
    if word.islower():
        return "Not an upper camel case string!"
    lower = []
    for i in string[1:]:
        if i.islower():
            word += i
        else:
            lower.append(word.lower())
            word = i
    if string[-1].isupper():
        lower.append(word.lower())
    return "_".join(lower)

print(camel_to_lower("SomeStringInCamelABC"))
print(camel_to_lower("anotherCamelCase"))