# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), и с помощью полученного объекта dict_items создайте
# новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями –
# числа.


if __name__ == '__main__':
    lis = {1: "lll", 2: "ooo", 3: "zzz"}
    temp = lis.items()
    lis_end = {}
    print(lis)

    for key, item in temp:
        lis_end.update({item: key})

    print(lis_end)
