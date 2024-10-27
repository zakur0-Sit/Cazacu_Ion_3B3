def intersectie(a, b):
    return [i for i in a if i in b]

def reuniune(a, b):
    return a + [i for i in b if i not in a]

def a_minus_b(a, b):
    return [i for i in a if i not in b]

def b_minus_a(a, b):
    return [i for i in b if i not in a]

def lists_operations(a, b):
    return [set(intersectie(a, b)), set(reuniune(a, b)), set(a_minus_b(a, b)), set(b_minus_a(a, b))]

print(lists_operations([2, 5, 7, 12, 18, 23], [3, 7, 9, 12, 20, 23]))
print(lists_operations([1, 4, 6, 8, 11, 19], [4, 6, 10, 15, 19, 21]))