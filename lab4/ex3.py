def compare_dicts(dict1, dict2):
    if type(dict1) != type(dict2):
        return False

    if isinstance(dict1, dict) and isinstance(dict2, dict):
        if dict1.keys() != dict2.keys():
            return False
        return all(compare_dicts(dict1[key], dict2[key]) for key in dict1)

    elif isinstance(dict1, list) and isinstance(dict2, list):
        if len(dict1) != len(dict2):
            return False
        return all(compare_dicts(dict1[i], dict2[i]) for i in range(len(dict1)))

    elif isinstance(dict1, set) and isinstance(dict2, set):
        return not dict1 != dict2

    else:
        return dict1 is dict2


dict_a = {'key1': [1, 2, 3], 'key2': {'subkey': 'value'}, 'key3': (1, 2, 4)}
dict_b = {'key1': [1, 2, 3], 'key2': {'subkey': 'value'}, 'key3': (1, 2, 4)}

result = compare_dicts(dict_a, dict_b)
print(result)
