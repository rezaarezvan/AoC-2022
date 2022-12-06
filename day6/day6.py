with open('input') as f:
    txt = f.read()

off = 4

for i in range(0, len(txt) - off):
    packet = txt[i : i + off]
    if len(set(packet)) == off:
        print(i + off)
        break
