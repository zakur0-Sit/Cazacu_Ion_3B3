def prime(arr):
    prime_list = []
    flag = False
    for num in arr:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                flag = True
                break
        if flag is False:
            prime_list.append(num)
        flag = False
    return prime_list
print(prime([3, 5, 8, 12, 15, 19, 23]))
print(prime([4, 6, 9, 11, 13, 16, 22, 29]))