lines = [line.strip() for line in open('input')]

pwd = []
csize = {}

for line in lines:
    if line == '$ cd /':
        pwd.append('/')
    elif line == '$ cd ..':
        pwd.pop()
    elif line.split()[0] == '$' and line.split()[1] == 'cd':
        pwd.append(line.split()[2])
    elif line == '$ ls':
        continue
    elif line.split()[0] == 'dir':
        continue
    elif str(line.split()[0]).isdigit():
        t = pwd[:]
        for p in range(len(t)):
            k = "/".join(t)
            if k not in csize:
                csize[k] = int(line.split()[0])
                t.pop()
            else:
                temp = csize[k]
                res = temp + int(line.split()[0])
                csize.update({k: res})
                t.pop()

# Part 1
ans = {k:v for (k,v) in csize.items() if v <= 100_000}
print(sum(ans.values()))

# Part 2
TOTAL_SIZE = 70000000
REQUIRED_SIZE = 30000000

space: int = TOTAL_SIZE - csize['/']
req: int = REQUIRED_SIZE - space

ans = {k:v for (k,v) in csize.items() if v >= req}
print(min(ans.values()))
