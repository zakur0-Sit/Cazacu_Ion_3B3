def count_one_bits(number):
    return str(bin(number)).count("1")

print(count_one_bits(24))