import random

path = "teams.txt"
f =open(path, "r", encoding="utf-8")

# teams - list of imported clubs from file
teams = []

# here I import clubs, atrr strip() - delete char of new line
for line in f:
    line = line.strip("\n")
    teams.append(line)

# shuffle element in list
random.shuffle(teams)

# schedule - list with another lists in correct order
schedule = []

# add first
schedule.append(teams)
print(schedule)

old_day = teams.copy()
end = len(teams) -1

# add another days -> days: n-1 , where n is count of clubs
for day in range(1,end):

    # new day: first team from prev list, last team from prev list + teams from prev list moved 1 position right
    new_day = [old_day[0],old_day[-1]]
    for team in range(1,end):
        new_day.append(old_day[team])

    # Done! Add new complete day to list.
    schedule.append(new_day)
    old_day = new_day

print(schedule)
