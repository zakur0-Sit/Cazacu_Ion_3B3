def tuples_generator(*args):
    tuples_list = []

    for i in range(max(len(args_list) for args_list in args)):
        new_tuple = ()
        for elem in args:
            if i < len(elem):
                new_tuple += (elem[i],)
            else:
                new_tuple += (None,)
        tuples_list.append(new_tuple)

    return tuples_list

print(tuples_generator([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
print(tuples_generator([1, 2, 3], [5, 6], ["a", "b", "c", "d"], [1, "a", True, 0]))