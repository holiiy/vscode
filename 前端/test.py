from collections import Counter

def find_first_unique_char(string):
    counter = Counter(string)
    for char, count in counter.items():
        if count == 1:
            return char
    return None
string = input()
print(find_first_unique_char(string))