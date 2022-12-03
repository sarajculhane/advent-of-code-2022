# AOC Day 1

# parse data to an array
with open('day-1/input.txt') as f:
    lines = f.readlines()
    elfs_data = []

    for line in lines:
        elf = []
        cleaned_line = line.strip().split('\n')
        if not cleaned_line[0]:
            cleaned_line[0] = 'skip'

        stringify = ''.join([item for item in cleaned_line])
        elfs_data.append(stringify)

# parse data to list of list by each elf


def get_data_by_elf():
    by_elf = []
    item = []
    # i = 0
    for i in range(len(elfs_data) - 1):
        if elfs_data[i] != 'skip':
            item.append(int(elfs_data[i]))
        else:
            by_elf.append(item)
            item = []
    return by_elf


data_by_elf = get_data_by_elf()

values = [sum(elf_value) for elf_value in value_list]

# Question 1: Find elf with Max value


def find_max(value_list):
    max_index = values.index(max(values))
    return values[max_index]

# Question 2: Find top 3 elves with Max value


def find_sum_by_top_num(value_list, num_eleves):
    return sum(sorted(values, reverse=True)[0: num_eleves])
