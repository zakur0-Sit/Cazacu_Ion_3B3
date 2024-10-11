def extract_number(string):
    number = ""
    for i in range(len(string)):
        if string[i].isnumeric() and number == "":
            number = string[i]
        elif string[i].isnumeric() and string[i-1].isnumeric():
            number += string[i]
        elif string[i].isalpha() and len(number) > 0:
            break
    return number

print(extract_number("abc123abc"))
print(extract_number("ab12ab34cd31"))
print(extract_number("An apple is 123 USD"))