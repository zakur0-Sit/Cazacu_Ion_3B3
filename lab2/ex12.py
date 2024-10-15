def rhyme(arr):
    rime_list = []
    processed_words = set()

    for i in range(len(arr)):
        if arr[i] in processed_words:
            continue
        rhyme_words = [arr[i]]
        for j in range(i + 1, len(arr)):
            if arr[i][-2:] == arr[j][-2:]:
                rhyme_words.append(arr[j])
                processed_words.add(arr[j])
        processed_words.add(arr[i])
        rime_list.append(rhyme_words)

    return rime_list

print(rhyme(["ana", "banana", "carte", "arme", "parte"]))
