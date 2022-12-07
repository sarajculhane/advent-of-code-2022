
# AOC Day 5
#
# parse data to an array
with open('day-5/input.txt') as f:
    lines = f.readlines()
    data = []
    more = []
    i = 0
    split_index = 0
    for line in lines:
        cleaned_line = line.split('\n')
        i += 1
        if not cleaned_line[0]:
            split_index = i
        data.append(cleaned_line)
    stacks = [''.join(item) for item in data[0: split_index - 1]]
    stacks = [item.replace(' ', '-').replace(
        '[', '-').replace(']', '-') for item in stacks]
    numbered = stacks[len(stacks) - 1:]
    stacks = stacks[:len(stacks) - 1]
    parsed_stacks = []


# parsing functions for starting stacks and moves
def get_start_stacks(stacks):
    parsed_stacks = []
    for i in range(len(numbered[0]) + 1):
        col = []
        for item in stacks:
            if len(item) > i and item[i] != '-':
                col.append(item[i])
        if len(col):
            parsed_stacks.append(col)
    [item.reverse() for item in parsed_stacks]

    return parsed_stacks


parsed_stacks = get_start_stacks(stacks)


def get_moves(data):
    moves = data[split_index:]
    moves = [''.join(item) for item in moves]
    moves = [item.replace('move', '').replace(
        'from', '').replace('to', '').strip() for item in moves]
    return moves


def get_actions(data):
    moves = get_moves(data)
    actions = []
    for move in moves:
        items = list(filter(lambda item: item != '', move.split(' ')))
        total_moves, start, target = [int(item) for item in items]
        actions.append({"total_moves": total_moves,
                       "start": start - 1, "target": target - 1})
    return actions
###

# Question 1 - Move one at a time
#
# Stack Implementation


class Stack:
    def __init__(self, stack):
        self.stack = [*''.join(stack)]

    def pop(self):
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def get(self):
        return self.stack
    def pop_many(self, num):
        popped = []
        for _ in range(num):
            popped.append(self.stack.pop())
            # print(self.stack.pop())
        print(popped, 'pop')
        return popped
    def size(self):
        return len(self.stack)
    def push_many(self, items):
        self.stack.extend(items)


def stackify(stacks):
    return list(map(lambda stack: Stack(stack), stacks))


# map each item in list to a stack
new_stacks = stackify(parsed_stacks)

def move_items(move, stacks):
    start_stack = stacks[move["start"]]
    target_stack = stacks[move["target"]]
    moves = move["total_moves"]

    for _ in range(moves):
        popped = start_stack.pop()
        target_stack.push(popped)


def rearrange_stacks(stacks):
    moves = get_actions(data)

    [move_items(move, stacks) for move in moves]


# Perform the rearranging
rearrange_stacks(new_stacks)


def peek_all(stacks):
    copy_stacks = stacks
    string = ''
    for i in range(len(copy_stacks)):
        string += copy_stacks[i].peek()
        print(copy_stacks[i])
    return string

# Question 2 - Multiple items at once




def move_many_items(move, stacks):
    start_stack = stacks[move["start"]]
    target_stack = stacks[move["target"]]
    moves = move["total_moves"]
    popped = start_stack.pop_many(moves)
    popped.reverse()
    target_stack.push_many(popped)

def rearrange_stacks_many(stacks):
    moves = get_actions(data)

    [move_many_items(move, stacks) for move in moves]

rearrange_stacks_many(new_stacks)

