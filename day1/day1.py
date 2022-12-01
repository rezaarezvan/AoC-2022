X = [l.strip() for l in open('input')]

Q = []
for elf in ('\n'.join(X)).split('\n\n'):
    q = 0
    for x in elf.split('\n'):
        q += int(x)
    Q.append(q)

Q.sort()

# Part 1
print(Q[-1])

# Part 2
print(Q[-1]+Q[-2]+Q[-3])
