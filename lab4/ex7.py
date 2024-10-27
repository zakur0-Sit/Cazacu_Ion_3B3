def sets_operations(*args):
    operation_dict = {}
    for first in range(len(args)):
        for second in range(first + 1, len(args)):
            set1, set2 = args[first], args[second]
            operation_dict.update({f"{set1} | {set2}": set1 | set2})
            operation_dict.update({f"{set1} & {set2}": set1 & set2})
            operation_dict.update({f"{set1} - {set2}": set1 - set2})
            operation_dict.update({f"{set2} - {set1}": set2 - set1})
    return operation_dict

print(sets_operations({1, 2}, {2, 3}))
print(sets_operations({10, 20, 30}, {20, 40}, {30, 50}))

# dictionar = sets_operations({1, 2}, {2, 3})
# for key in dictionar:
#     print(key, dictionar[key])