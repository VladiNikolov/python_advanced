bomb_effects = [int(i) for i in input().split(", ")]
bomb_casings = [int(i) for i in input().split(", ")]

bomb_dict = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}
collected_bombs = False

while bomb_effects and bomb_casings:
    effect = bomb_effects.pop(0)
    casing = bomb_casings.pop()

    result = effect + casing

    if result == 40:
        bomb_dict["Datura Bombs"] += 1
    elif result == 60:
        bomb_dict["Cherry Bombs"] += 1
    elif result == 120:
        bomb_dict["Smoke Decoy Bombs"] += 1
    else:
        bomb_effects.insert(0, effect)
        bomb_casings.append(casing - 5)

    if bomb_dict["Cherry Bombs"] >= 3 and bomb_dict["Datura Bombs"] >= 3 and bomb_dict["Smoke Decoy Bombs"] >= 3:
        collected_bombs = True
        break
if collected_bombs:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(i) for i in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(i) for i in bomb_casings])}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {bomb_dict['Cherry Bombs']}")
print(f"Datura Bombs: {bomb_dict['Datura Bombs']}")
print(f"Smoke Decoy Bombs: {bomb_dict['Smoke Decoy Bombs']}")


