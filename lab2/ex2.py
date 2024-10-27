def vowels_count_func(string):
    vowels_arr = ["a", "i", "u", "e", "o"]
    vowels_count = 0

    for i in string:
        if i in vowels_arr:
            vowels_count += 1
    return vowels_count

    # return sum(1 for i in string if i in ["a", "i", "u", "e", "o"])

print(vowels_count_func("something"))
