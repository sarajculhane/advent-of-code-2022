# AOC Day 4
#
# parse data to an array
with open('day-4/input.txt') as f:
    lines = f.readlines()
    items = []

    for line in lines:
        cleaned_line = line.strip().split('\n')
        array = [item for item in cleaned_line]
        array = ''.join([item for item in array])
        items.append(array)


def parse_bound(bound_str):
    low, high = map(lambda item: int(item),  bound_str.split('-'))
    return [low, high]


def has_overlap(item):
    first, second = parse_bound(item[0]), parse_bound(item[1])
    check_left = check_bounds_any(first, second)
    check_right = check_bounds_any(second, first)

    return check_left or check_right


def count_overlaps(data):
    count = 0
    for item in data:
        item_str = ''.join(item).split(',')
        if has_overlap(item_str):
            count += 1
    return count


# Question 1: Fully inclusive
def check_bounds(arr1, arr2):
    arr1_low, arr1_high = arr1
    arr2_low, arr2_high = arr2
    if arr1_low >= arr2_low and arr1_high <= arr2_high:
        return True
    else:
        return False

# Question 2: Has any intersection


def check_bounds_any(arr1, arr2):
    arr1_low, arr1_high = arr1
    arr2_low, arr2_high = arr2
    if arr1_high < arr2_low or arr2_high < arr1_low:
        return False
    else:
        return True
