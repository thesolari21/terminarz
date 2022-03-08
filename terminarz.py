import random

def importFile():
    path = "teams.txt"

    try:
        f = open(path, "r", encoding="utf-8")
    except FileNotFoundError:
        teams = ["Brak pliku!"]
        return teams

    # teams - list of imported clubs from file
    teams = []

    # here I import clubs, atrr strip() - delete char of new line
    for line in f:
        line = line.strip("\n")
        teams.append(line)

    if len(teams) % 2 != 0:
        teams.append("X")

    f.close()
    return teams

def makeSchedule(teams):
    # shuffle element in list
    random.shuffle(teams)

    # schedule - list with another lists in correct order
    schedule = []

    # add first
    schedule.append(teams)

    old_day = teams.copy()
    end = len(teams) - 1

    # add another days -> days: n-1 , where n is count of clubs
    for day in range(1, end):

        # new day: first team from prev list, last team from prev list + teams from prev list moved 1 position right
        new_day = [old_day[0], old_day[-1]]
        for team in range(1, end):
            new_day.append(old_day[team])

        # Done! Add new complete day to list.
        schedule.append(new_day)
        old_day = new_day

    return schedule

def dispSchedule(schedule):
    # to display round
    day = 1

    for i in schedule:
        count = 1
        print("Kolejka:", day)

        # call next teams in round, display 2 teams in 1 line
        for j in i:
            if count % 2 != 0:
                print(j, "- ", end="")
                count = count + 1
            else:
                print(j)
                count = count + 1
        print(end="\n")
        day = day + 1

def exportSchedule(schedule):
    # same as dispSchedule but does not display on screen, now export to file
    # print parameter FILE -> redirect a stream to a file - helpfull!
    f = open("export.txt", "w")

    day = 1

    for i in schedule:
        count = 1
        print("Kolejka:", day, file = f)

        # call next teams in round, display 2 teams in 1 line
        for j in i:
            if count % 2 != 0:
                print(j, "- ", end="" , file = f)
                count = count + 1
            else:
                print(j , file = f)
                count = count + 1
        print(end="\n" , file = f)
        day = day + 1

    f.close()

# MAIN FUNCTION #
teams = importFile()
schedule = makeSchedule(teams)
dispSchedule(schedule)
exportSchedule(schedule)