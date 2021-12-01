with open("input.txt", "r") as f:
    data = [int(d.rstrip()) for d in f.readlines()]

res = []
#  1 - indicates increasing than previous
# -1 - indicates decreasing than previous
for i in range(len(data)):
    if i == 0:
        res.append(None)
        continue
    if data[i] > data[i-1]:
        res.append(1)
    else:
        res.append(-1)

print(res.count(1))

