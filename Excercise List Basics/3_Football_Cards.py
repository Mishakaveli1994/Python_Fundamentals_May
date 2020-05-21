team_a = [i for i in range(1, 12)]
team_b = [i for i in range(1, 12)]

cards = input().split(' ')
terminated = 0
for i in cards:
    team, player = i[0], int(i[2:])
    if team == 'A':
        if player in team_a:
            team_a.pop(team_a.index(player))
    elif team == 'B':
        if player in team_b:
            team_b.pop(team_b.index(player))
    if len(team_a) < 7 or len(team_b) < 7:
        terminated = 1


print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if terminated == 1:
    print("Game was terminated")
