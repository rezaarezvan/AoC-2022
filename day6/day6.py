with open('input') as f:
    txt = f.read()

off = 14

for i in range(0, len(txt) - 4):
    packet = txt[i : i + off]
    if len(set(packet)) == off:
        print(i + off)
        break
