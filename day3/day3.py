IN = [l.split() for l in open('input')]

s1 = 0
s2 = 0
points = {x : e + 1 for e, x in enumerate([chr(y) for y in range(97, 123)] + [chr(y) for y in range(65, 91)])}

for i, x in enumerate(IN):
    m = len(x[0]) // 2
    s1 += points[next(iter(set(x[0][ : m]).intersection(set(x[0][m : ]))))]

    if not i % 3:
        badge = set(x[0])
        continue
    badge &= set(x[0])
    if i % 3 == 2:
        s2 += points[next(iter(badge))]

print(s1)
print(s2)
