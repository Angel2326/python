from functools import reduce


def new_spis(a, b):
    if a < b:
        new_spisok.append(b)
    return b


new_spisok = []
new_spisok.append(reduce(new_spis, [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]))
print(new_spisok)
