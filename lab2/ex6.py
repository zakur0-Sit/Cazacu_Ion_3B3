def x_appearance(x, *arrays):
    appear = {}
    for arr in arrays:
        for i in arr:
            if i in appear:
                appear[i] += 1
            else:
                appear[i] = 1

    x_appear = []
    for key in appear:
        if appear[key] == x:
            x_appear.append(key)

    return x_appear

print(x_appearance(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
print(x_appearance(1, [1, "dog", 5], [2, "cat", 21], [1, "dog", 21, 7], [3, "fish", 7]))