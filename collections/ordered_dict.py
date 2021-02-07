from collections import OrderedDict

def main():
    sport_teams = [
        ("Royals", (18, 12)),
        ("Rockets", (24, 6)),
        ("Cardinals", (20, 10)),
        ("Dragons", (22, 8))
    ]

    sorted_teams = sorted(sport_teams, key=lambda t: t[1][0], reverse=True)

    print(sorted_teams)

    # Creating orderdict
    teams = OrderedDict(sorted_teams)
    print(teams)

    # Pop
    team, wl = teams.popitem(False)
    print("Best", team, wl)

    for i, team in enumerate(teams):
        print(i, team)




if __name__ == "__main__":
    main()
    