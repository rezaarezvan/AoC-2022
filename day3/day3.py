with open("input", "r") as file:
    data = file.read().splitlines()

    points = {x : e + 1 for e, x in enumerate([chr(y) for y in range(97, 123)] + [chr(y) for y in range(65, 91)])}
    p1, p2 = 0, 0

    for e, x in enumerate(data):
        p1 += points[next(iter(set(x[:len(x) // 2]) & set(x[len(x) // 2:])))]
        
        if not e % 3:
            badge = set(x)
            continue
        badge &= set(x)

        if e % 3 == 2:
            p2 += points[next(iter(badge))]

    print(p1)
    print(p2)
