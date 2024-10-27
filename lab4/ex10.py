def loop(mapping):
    loop_key = mapping["start"]
    loop_list = [loop_key]
    while True:
        if not mapping[loop_key] in loop_list:
            loop_list += mapping[loop_key]
            loop_key = mapping[loop_key]
        else:
            break
    return loop_list

print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))