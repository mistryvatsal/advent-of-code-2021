with open("input.txt", "r") as f:
    data = f.read().splitlines()
data = [d.split(" ") for d in data]

horizontal = 0
depth = 0

for ele in data:
    if ele[0] == "forward":
        horizontal += int(ele[1])
    elif ele[0] == "down":
        depth += int(ele[1])
    elif ele[0] == "up":
        depth -= int(ele[1])
    else:
        pass

print(horizontal * depth)