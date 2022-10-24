from collections import deque

bomb_effects = deque([int(i) for i in input().split(", ")])
bomb_casings = deque([int(i) for i in input().split(", ")])

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0
collected_bombs = False

while bomb_effects and bomb_casings:

    effects = bomb_effects.popleft()
    casings = bomb_casings.pop()

    result = effects + casings

    if result == 40:
        datura_bombs += 1
    elif result == 60:
        cherry_bombs += 1
    elif result == 120:
        smoke_decoy_bombs += 1
    else:
        bomb_effects.appendleft(effects)
        bomb_casings.append(casings - 5)
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        collected_bombs = True
        break

if collected_bombs:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bomb_effects) == 0:
    print(f"Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")

if len(bomb_casings) == 0:
    print(f"Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")