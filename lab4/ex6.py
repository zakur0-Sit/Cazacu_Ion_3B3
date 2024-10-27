def unique_duplicate(array):
    elements_set = set(array)
    unique = 0
    duplicate = 0
    for element in elements_set:
        if array.count(element) > 1:
            duplicate += 1
        else:
            unique += 1

    return unique, duplicate

print(unique_duplicate(["mere", "pere", "prune", "mere", "caise", "prune", "piersici", "capsuni", "caise", "banane"]))