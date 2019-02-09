drzewa = ['sosna', 'topola', 'dab', 'buk']
for s in drzewa:
    print(s)

    for idx in range(len(drzewa)):
        print("idx: " + str(idx) + " : " + drzewa[idx])

l = drzewa[:2]
for l in drzewa:
    print(l)
