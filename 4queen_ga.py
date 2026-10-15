def conflicts(chromosome):
    n = len(chromosome)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):

            if chromosome[i] == chromosome[j]:
                count += 1

            if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                count += 1

    return count


population = [
    [2, 4, 3, 1],
    [1, 2, 3, 4],
    [2, 1, 3, 2],
    [4, 3, 1, 1]
]

print("Generation 0")
for p in population:
    print(p, "Conflicts =", conflicts(p))

for gen in range(1, 3):

    new_population = []

    for i in range(0, len(population), 2):

        p1 = population[i]
        p2 = population[(i + 1) % len(population)]

        child1 = p1[:2] + p2[2:]
        child2 = p2[:2] + p1[2:]

        new_population.append(child1)
        new_population.append(child2)

    population = new_population

    print("\nGeneration", gen)

    for p in population:
        print(p, "Conflicts =", conflicts(p))