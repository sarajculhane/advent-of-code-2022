# AOC Day 2
#
# parse data to an array
with open('day-2/input.txt') as f:
    lines = f.readlines()
    match_data = []

    for line in lines:
        elf = []
        cleaned_line = line.strip().split('\n')
        array = ''.join([item for item in cleaned_line])
        array = ''.join([item.strip() for item in array])
        match_data.append(array)

values = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Z": 2,
    "Y": 3,
}

result = {
    "win": 6,
    "draw": 3,
    "loss": 0,
}

outcomes = {
    'A': {
        'Y': 'loss',
        'X': 'draw',
        'Z': 'win',
    },
    'B': {
        'Y': 'draw',
        'X': 'win',
        'Z': 'loss',
    },
    'C': {
        'Y': 'win',
        'X': 'loss',
        'Z': 'draw',
    },
}


def calculate_score(data):
    score = 0
    for game in data:
        opponent, player = game
        outcome = outcomes[opponent][player]
        score += result[outcome] + values[player]
    return score


weakness = {
    "A": "B",
    "B": "C",
    "C": "A"
}
strength = {
    "B": "A",
    "C": "B",
    "A": "C"
}


def calculate_score_new_strategy(data):
    score = 0
    for match in data:
        if match[1] == "X":
            score += result["loss"] + values[strength[match[0]]]
        elif match[1] == "Y":
            score += result["draw"] + values[match[0]]
        elif match[1] == "Z":
            score += result["win"] + values[weakness[match[0]]]
    return score
