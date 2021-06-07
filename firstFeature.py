"""Трансформирует символы строки в ascii графику"""
import json

STRING_LIST_SIZE = 7

with open("symbols.json", 'r') as file:
    symballs = json.loads(file.read())
    a = symballs["а"]


def transformStrList(s, symbols=symballs):
    s = s.lower()
    result = [""] * STRING_LIST_SIZE
    for small_symbol in s:
        for i in range(STRING_LIST_SIZE):
            result[i] += symballs[small_symbol][i]
    return result


def transformString(s):
    str_list = transformStrList(s)
    result = '\n'.join(str_list)
    return result


def transformLongString(s):
    for i in range(0,len(s),7):
        yield transformString(s[i:i+7])


def main():
    s = ""
    while s != "-1":
        s = input("А?:")
        t = transformString(s)
        print(t)
        print("\n\n\n")


if __name__ == "__main__":
    main()
