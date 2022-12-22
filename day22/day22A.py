import re

*MAP, _, PATH = open('input')
position, dir = MAP[0].index('.'), 1

PATH = re.findall(r'\d+|[RL]', PATH)
MAP = {complex(x, y): c for y, l in enumerate(MAP)
       for x, c in enumerate(l) if c in '.#'}

for path in PATH:
    if path == 'R':
        dir *= 1j
    elif path == 'L':
        dir *= -1j
    else:
        for _ in range(int(path)):
            new_pos = position + dir
            if new_pos in MAP:
                if MAP[new_pos] == '.':
                    position = new_pos
            else:  # wrap
                new_pos = position
                while new_pos - dir in MAP:
                    new_pos -= dir
                if MAP[new_pos] == '.':
                    position = new_pos

print(int(1000*(position.imag+1) + 4 *
      (position.real+1) + [1, 1j, -1, -1j].index(dir)))
