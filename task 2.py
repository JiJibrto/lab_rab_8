# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# создайте словарь, связав его с переменной school , и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
# (удален) другой класс. Вычислите общее количество учащихся в школе.

if __name__ == '__main__':
    school = {"1a": 23, "2b": 15, "3c": 10}

    while True:
        command = input("Enter command> ").lower()

        if command == "exit":
            break

        # первое задание
        if command == "change":
            name = str(input("Enter class to change> "))
            qua = int(input("Enter the number of students> "))
            school[name] = qua

        # второе задание
        if command == "add":
            name = str(input("Enter name of new class> "))
            qua = int(input("Enter the number of students> "))
            school.update({name: qua})

        # третье задание
        if command == "del":
            name = str(input("Enter class to delete> "))
            school.pop(name)

        if command == "list":
            print(school)



