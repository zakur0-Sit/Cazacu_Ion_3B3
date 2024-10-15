def compose(notes, moves, start):
    notes_order = [notes[start]]
    for i in moves:
        start += i
        if start > len(notes):
            start = start - len(notes)
        if start < 0:
            start = len(notes) - start
        notes_order.append(notes[start])

    return notes_order

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))