"""
cricket matches find total points win points = 4, and tie points = 2
"""

games_total = int(input("Enter total games : "))
games_win = int(input("Games win: "))
games_lost = int(input("Games lost: "))
games_tied = games_total - games_win - games_lost

Points = (games_win * 4) + (games_tied * 2)

print(f"Total Points : {Points}")
# print(games_tied)
