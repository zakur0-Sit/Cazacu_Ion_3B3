# def intersection(a, b):
#     intersection_list = []
#     for i in a:
#         if i in b:
#             intersection_list.append(i)
#     return intersection_list
#
# def reunion(a, b):
#     reunion_list = a.copy()
#     for i in b:
#         if i in a:
#             continue
#         else:
#             reunion_list.append(i)
#     return reunion_list
#
# def a_minus_b(a, b):
#     a_minus_b_list = a.copy()
#     for i in b:
#         if i in a_minus_b_list:
#             a_minus_b_list.remove(i)
#     return a_minus_b_list
#
# def b_minus_a(a, b):
#     b_minus_a_list = b.copy()
#     for i in a:
#         if i in b_minus_a_list:
#             b_minus_a_list.remove(i)
#     return b_minus_a_list

# ceva mai frumos

def intersectie(a, b):
    return [i for i in a if i in b]

def reuniune(a, b):
    return a + [i for i in b if i not in a]

def a_minus_b(a, b):
    return [i for i in a if i not in b]

def b_minus_a(a, b):
    return [i for i in b if i not in a]

def lists_operations(a, b):
    return "Intersectie : " + str(intersectie(a, b)) + "\nReuniune : " + str(reuniune(a, b)) + "\nA \\ B : " + str(a_minus_b(a, b)) + "\nB \\ A : " + str(b_minus_a(a, b)) + "\n"

print(lists_operations([2, 5, 7, 12, 18, 23], [3, 7, 9, 12, 20, 23]))
print(lists_operations([1, 4, 6, 8, 11, 19], [4, 6, 10, 15, 19, 21]))