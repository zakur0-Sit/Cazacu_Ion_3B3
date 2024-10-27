def special_sort(arr):
    sorted_list = sorted(arr, key=lambda x: x[1][2])

    return sorted_list

print(special_sort([("abc", "bcd"), ("abc", "zzb"), ("zsa", "aaa")]))