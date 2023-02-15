# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    success = "Success"
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
    
        if next in ")]}":
            if not opening_brackets_stack:
                return str(i + 1)
            lastel = opening_brackets_stack.pop()
            if not are_matching(lastel.char, next):
                return str(i + 1)
    if opening_brackets_stack:
        lastel = opening_brackets_stack
        return str(lastel.position + 1)
    
    return success
def main():
    text = input()
    if text[0] == "I":
        text = input();
        mismatch = find_mismatch(text);
        print(mismatch)
if __name__ == "__main__":
    main()
