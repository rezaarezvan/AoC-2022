CHOICES = ("S", "P", "R")

OPPONENT = {
    "A": CHOICES[2],
    "B": CHOICES[1],
    "C": CHOICES[0]
}

PLAYER = {
    "X": CHOICES[2],
    "Y": CHOICES[1],
    "Z": CHOICES[0]
}


def get_score(opponent_choice, player_choice):
    opp_val = CHOICES.index(OPPONENT[opponent_choice])
    ply_val = CHOICES.index(PLAYER[player_choice])

    result = len(CHOICES) - CHOICES.index(PLAYER[player_choice])

    table = {
        -1: 6,
        0: 3,
        2: 6,
    }

    return result + table.get((ply_val - opp_val), 0)


def main(part=1):
    score = 0
    with open("input", "r") as f:
        rounds = [line.rstrip("\n").split() for line in f.readlines()]

        for round in rounds:
            if part == 1:
                score += get_score(round[0], round[1])

            else:
                player_scores_from_key = list(
                    map(lambda key: get_score(round[0], key), list(PLAYER.keys())))

                if round[1] == "X":
                    score += min(player_scores_from_key)

                elif round[1] == "Z":
                    score += max(player_scores_from_key)

                else:
                    opponent_choice_to_player = list(
                        filter(lambda item: item[1] == OPPONENT[round[0]], list(PLAYER.items())))[0][0]
                    score += get_score(round[0], opponent_choice_to_player)

        return score

print(f'First part: {main()}')
print(f'Second part: {main(part=2)}')
