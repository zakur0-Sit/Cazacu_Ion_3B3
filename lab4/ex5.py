def validate_dict(rules, dictionary):
    for key, value in dictionary.items():
        key_flag = False
        for subrules in rules:
            if key == subrules[0]:
                key_flag = True
                if not value.startswith(subrules[1]):
                    return False

                if not value.endswith(subrules[3]):
                    return False

                pref_len = len(subrules[1])
                suf_len = len(subrules[3])

                if subrules[2] not in value[pref_len: len(value) - suf_len]:
                    return False
        if not key_flag:
            return False
    return True

print(validate_dict({("key1", "abc", "mid", "xyz"), ("key2", "", "inner", "")}, {"key1": "abc123mid456xyz", "key2": "inner_value"}))
print(validate_dict({("key1", "a", "b", "c"), ("key2", "x", "", "y")}, {"key1": "abc", "key2": "xy", "key3": "z"}))