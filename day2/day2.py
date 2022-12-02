IN = [l.split() for l in open('input')]

R = {
    "A": 1, # rock
    "B": 2, # ppaer
    "C": 3, # sciss
}
Q = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

S = 0
for a, b in IN:
    if R[a] == Q[b]:
        S += 3
    elif (
        (a == "A" and b == "Y") or (a == "B" and b == "Z") or (a == "C" and b == "X")
    ):
        S += 6
    S += Q[b]
    
print(S)

S = 0
for a, b in IN:
    O = None
    if b == "X":
        S += 0
        if a == "A":
            O = "Z"
        elif a == "B":
            O = "X"
        else:
            O = "Y"
    elif b == "Y":
        S += 3
        if a == "A":
            O = "X"
        elif a == "B":
            O = "Y"
        else:
            O = "Z"
    else:
        S += 6
        if a == "A":
            O = "Y"
        elif a == "B":
            O = "Z"
        else:
            O = "X"
    
    S += Q[O]
    
print(S)
