def char_count(string):
    char_dict = {}
    for char in string:
        char_dict.update({char: string.count(char)})
    return char_dict
print(char_count("Ana has apples."))