# AOC Day 3
#
# parse data to an array
with open('day-3/input.txt') as f:
    lines = f.readlines()
    items = []

    for line in lines:
        cleaned_line = line.strip().split('\n')
        array = ''.join([item for item in cleaned_line])
        items.append(array)


# Helper func to get alpha values
def get_char_value(char):
    val = ord(char.lower()) - 96
    if char.upper() == char:
        val += 26
    return val

# calc priority values


def get_priority_value(items):
    chars = []
    for item in items:
        split = [set(item[0:(round(len(item) / 2))]),
                 set(item[round(len(item) / 2):len(item)])]

        diff = split[0].intersection(split[1])
        chars.append(diff.pop())
    return chars

# Question 1


def calculate_scores(data):
    items = get_priority_value(data)
    char_vals = [get_char_value(item) for item in items]

    return sum(char_vals)

# Question 2 - by group size 3


def group_rows(data, size):
    array = []
    i = 0
    for i in range(0, len(data), size):
        array.append(data[i: i + size])
    return array


def intersection(items):
    chars = []
    data = group_rows(items, 3)
    for item in data:
        diff = set.intersection(*map(set, item)).pop()
        chars.append(diff)
    return sum([get_char_value(item) for item in chars])
