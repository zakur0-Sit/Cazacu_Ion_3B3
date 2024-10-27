def spectators(arr):
    can_not_see_list = []

    for i in range(1, len(arr)):
        for j in range(len(arr[0])):
            for front in range(0, i):
                if arr[i][j] <= arr[front][j]:
                    can_not_see_list.append((i, j))
                    break

    return can_not_see_list

print(spectators([
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]))

print(spectators([
    [3, 4, 5, 4, 3, 3],
    [4, 7, 7, 5, 8, 4],
    [5, 7, 6, 6, 7, 5],
    [4, 8, 6, 6, 7, 4],
    [3, 5, 7, 7, 5, 3],
    [3, 4, 5, 4, 3, 3]
]))

