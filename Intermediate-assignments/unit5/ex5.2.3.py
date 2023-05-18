from itertools import combinations

bills = [20] * 3 + [10] * 5 + [5] * 2 + [1] * 5
options = set()

for r in range(1, len(bills) + 1):
    for comb in combinations(bills, r):
        if sum(comb) == 100:
            options.add(tuple(sorted(comb, reverse=True)))

for option in options:
    print(option)

print("Number of options:", len(options))
