# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, char in enumerate(text):
        if char in "([{":
            opening_brackets_stack.append(char)
            last_index_added = i
        elif char in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            else:
                last_char = opening_brackets_stack.pop()
                last_index_added = last_index_added -1
                if (last_char == "(" and char !=")") or (last_char == "{" and char !="}") or \
                (last_char == "[" and char !="]"):
                    return i+1
    if len(opening_brackets_stack)==0:
        return "Success"
    else:
        return last_index_added+1


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
