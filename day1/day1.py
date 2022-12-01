X = [l.strip() for l in open('input')]

Q = []
q = 0

for i in X:
    if i == '':
        Q.append(q)
        q = 0
    else:
        q += int(i)

Q.sort()

# Part 1
print(Q[-1])

# Part 2
print(Q[-1]+Q[-2]+Q[-3])
