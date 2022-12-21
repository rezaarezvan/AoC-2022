import re
import z3


def solve(name):
    ans = z3.Optimize()
    for line in open('input'):
        for monke in re.findall(r'[a-z]{4}', line):
            exec(f'{monke} = z3.Int("{monke}")')

        if name == 'humn':
            if line[:4] == 'humn':
                continue

            if line[:4] == 'root':
                line = line[6:].replace('+', '==')

        exec(f'ans.add({line.replace(":", "==")})')

    ans.check()
    return ans.model()[z3.Int(name)]


print(solve('root'), solve('humn'))
