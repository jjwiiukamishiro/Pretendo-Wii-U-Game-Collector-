print("==== Pretendo Wii U Collection Tracker ====")

game_count = int(input("How many Nintendo Wii U games do you own? "))
games = []

print("-----------------------------")

print("You own", game_count, "Nintendo Wii U games.")
print("-----------------------------")

for i in range(game_count):
    game = input("Whats the name of the Wii U Game? : ")
    games.append(game)
    print("Added", game)

print()
print()
print("-----------------------------")
print("Your Wii U collection:")
print("-----------------------------")

for i, game in enumerate(games, start=1):
    print(f"{i}. {game}")

print("-----------------------------")
print("Total games:", len(games))
