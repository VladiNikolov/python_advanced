from collections import deque

caffeine_milligrams = deque([int(i) for i in input().split(", ")])
energy_drink = deque([int(i) for i in input().split(", ")])

stamat_total = 0
stamat_max = 300
while caffeine_milligrams and energy_drink:

    caffeine = caffeine_milligrams.pop()
    drink = energy_drink.popleft()

    result = caffeine * drink
    if result <= stamat_max - stamat_total:
        stamat_total += result
    elif result > stamat_max - stamat_total:
        energy_drink.append(drink)
        if stamat_total - 30 > 0:
            stamat_total -= 30
        else:
            stamat_total = 0

if energy_drink:
    print(f"Drinks left: {', '.join(map(str, energy_drink))}")
elif len(energy_drink) == 0:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_total} mg caffeine.")