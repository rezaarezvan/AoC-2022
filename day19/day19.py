from collections import deque
IN = open('input').read().strip()
BLUEPRINTS = [x for x in IN.split('\n')]


def solve(cost_ore, cost_clay, cost_obsidian_ore, cost_obsidian_clay,
          cost_geode_ore, cost_geode_obsidian, TIME):
    BEST = 0
    INIT_STATE = (0, 0, 0, 0, 1, 0, 0, 0, TIME)
    Q = deque([INIT_STATE])
    SEEN = set()
    while Q:
        curr_state = Q.popleft()
        ore, clay, obsidian, geode,\
            ore_robot, clay_robot, obsidian_robot, geode_robot, time = curr_state

        BEST = max(BEST, geode)

        if time == 0:
            continue

        cost = max([cost_ore, cost_clay, cost_obsidian_ore, cost_geode_ore])

        if ore_robot >= cost:
            ore_robot = cost

        if clay_robot >= cost_obsidian_clay:
            clay_robot = cost_obsidian_clay

        if obsidian_robot >= cost_geode_obsidian:
            obsidian_robot = cost_geode_obsidian

        if ore >= time * cost - ore_robot * (time - 1):
            ore = time * cost - ore_robot * (time - 1)

        if clay >= time * cost_obsidian_clay - clay_robot * (time - 1):
            clay = time * cost_obsidian_clay - clay_robot * (time - 1)
        if obsidian >= time * cost_geode_obsidian - obsidian_robot * (time - 1):
            obsidian = time * cost_geode_obsidian - obsidian_robot * (time - 1)

        curr_state = (ore, clay, obsidian, geode, ore_robot,
                      clay_robot, obsidian_robot, geode_robot, time)

        if curr_state in SEEN:
            continue

        SEEN.add(curr_state)
        
        '''
        if len(SEEN) % 1000000 == 0:
            print(time, BEST, len(SEEN))
        '''

        assert ore >= 0 and clay >= 0 and obsidian >= 0 and geode >= 0, curr_state

        Q.append((ore + ore_robot, clay + clay_robot, obsidian + obsidian_robot,
                 geode + geode_robot, ore_robot, clay_robot, obsidian_robot, geode_robot, time - 1))

        if ore >= cost_ore:
            Q.append((ore-cost_ore + ore_robot, clay + clay_robot, obsidian +
                      obsidian_robot, geode + geode_robot, 
                      ore_robot + 1, clay_robot, obsidian_robot, geode_robot, time - 1))

        if ore >= cost_clay:
            Q.append((ore - cost_clay + ore_robot, clay + clay_robot, obsidian +
                      obsidian_robot, geode + geode_robot, 
                      ore_robot, clay_robot + 1, obsidian_robot, geode_robot, time - 1))

        if ore >= cost_obsidian_ore and clay >= cost_obsidian_clay:
            Q.append((ore - cost_obsidian_ore + ore_robot, clay-cost_obsidian_clay +
                      clay_robot, obsidian + obsidian_robot, geode + geode_robot, 
                      ore_robot, clay_robot, obsidian_robot + 1, geode_robot, time - 1))

        if ore >= cost_geode_ore and obsidian >= cost_geode_obsidian:
            Q.append((ore - cost_geode_ore + ore_robot, clay + clay_robot, obsidian -
                      cost_geode_obsidian + obsidian_robot, geode + geode_robot, 
                      ore_robot, clay_robot, obsidian_robot, geode_robot + 1, time - 1))

    return BEST


p1 = 0
p2 = 1
t1 = 24
t2 = 32

for i, blueprint in enumerate(BLUEPRINTS):
    words = blueprint.split()
    id_ = int(words[1][:-1])
    ore_cost = int(words[6])
    clay_cost = int(words[12])
    obsidian_cost_ore, obsidian_cost_clay = int(words[18]), int(words[21])
    geode_cost_ore, geode_cost_clay = int(words[27]), int(words[30])

    s1 = solve(ore_cost, clay_cost, obsidian_cost_ore,
               obsidian_cost_clay, geode_cost_ore, geode_cost_clay, t1)
    p1 += id_*s1

    if i < 3:
        s2 = solve(ore_cost, clay_cost, obsidian_cost_ore,
                   obsidian_cost_clay, geode_cost_ore, geode_cost_clay, t2)
        p2 *= s2

print(p1)
print(p2)
