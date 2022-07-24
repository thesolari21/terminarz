import random


def import_file():
    """
    Load text file from ./teams.txt.
    Convert to list Teams.
    If an odd number of teams, add team X.
    :return: list
    """

    path = "teams.txt"
    teams = []

    try:
        f = open(path, "r", encoding="utf-8")
    except FileNotFoundError:
        teams = ["Brak pliku!"]
        return teams

    for line in f:
        line = line.strip("\n")
        teams.append(line)

    if len(teams) % 2 != 0:
        teams.append("X")

    f.close()
    return teams


def make_schedule(teams):
    """
    Based on round robin tournament - https://en.wikipedia.org/wiki/Round-robin_tournament
    New round: first team from prev list, last team from prev list + teams from prev list moved 1 position right
    Extra: shuffle list, fix problem: only home games for first player
    :param teams: list
    :returns schedule: list
    """

    random.shuffle(teams)
    schedule = []
    schedule.append(teams)

    old_round = teams.copy()
    end = len(teams) - 1

    for day in range(1, end):
        new_round = [old_round[0], old_round[-1]]
        for team in range(1, end):
            new_round.append(old_round[team])

        old_round = new_round
        schedule.append(new_round)

        # fix only home games for first player
        if day % 2 == 0:
            schedule[day-1][0],  schedule[day-1][1] = schedule[day-1][1],  schedule[day-1][0]

    return schedule


def disp_schedule(schedule):
    """
    Display schedule with formatting
    :param schedule: list
    :return: None
    """

    round_number = 1

    for round in schedule:
        count = 1
        print("Kolejka:", round_number)

        for team in round:
            if count % 2 != 0:
                print(team, "- ", end="")
                count = count + 1
            else:
                print(team)
                count = count + 1
        print(end="\n")
        round_number = round_number + 1


def export_schedule(schedule):
    """
    Export schedule to text file with formatting
    (formatting like disp_schedule)
    :param schedule: list
    :return: None
    """

    f = open("export.txt", "w")

    round_number = 1

    for round in schedule:
        count = 1
        print("Kolejka:", round_number, file=f)

        for team in round:
            if count % 2 != 0:
                print(team, "- ", end="", file=f)
                count = count + 1
            else:
                print(team, file=f)
                count = count + 1
        print(end="\n", file=f)
        round_number = round_number + 1

    f.close()


if __name__ == "__main__":
    teams = import_file()
    schedule = make_schedule(teams)
    disp_schedule(schedule)
    export_schedule(schedule)
