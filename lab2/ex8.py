def ascii_div(x, arr, flag):
    word_list = []
    for word in arr:
        char_list = []
        for i in word:
            if flag is True:
                if ord(i) % x == 0:
                    char_list.append(i)
            else:
                if ord(i) % x != 0:
                    char_list.append(i)
        word_list.append(char_list)

    return word_list

print(ascii_div(2, ["test", "hello", "lab002"], False))
print(ascii_div(2, ["test", "hello", "lab002"], True))