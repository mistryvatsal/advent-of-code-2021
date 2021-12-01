with open("input.txt", "r") as f:
    data = [int(d.rstrip()) for d in f.readlines()]

res = []
sum_data = []

# Storing sum of 3 consecutive numbers, sliding window approad in sum_data list
for i in range(len(data)-2):
    sum_data.append(data[i]+data[i+1]+data[i+2])

#  1 - indicates increasing than previous
# -1 - indicates decreasing than previous
for i in range(len(sum_data)):
    if i == 0:
        res.append(None)
        continue
    if sum_data[i] > sum_data[i-1]:
        res.append(1)
    else:
        res.append(-1)

print(res.count(1))

