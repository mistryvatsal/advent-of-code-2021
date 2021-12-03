files = ["sample_input.txt", "input.txt"]
for file in files:
    with open(file) as f:
        data = [d.rstrip() for d in f.readlines()]

    masterdata = [list(d) for d in data]
    
    oxydata = [ele for ele in masterdata]
    co2data = [ele for ele in masterdata]

    n = len(data[0])
    
    for i in range(n):
        temp = []
        if len(oxydata) == 1:
            break
        for bin in oxydata:
            temp.append(bin[i])
        to_keep = '1' if temp.count('1') >= temp.count('0') else '0'
        oxydata = [ele for ele in oxydata if ele[i] == to_keep]

    for i in range(n):
        temp = []
        if len(co2data) == 1:
            break
        for bin in co2data:
            temp.append(bin[i])
        to_keep = '0' if temp.count('0') <= temp.count('1') else '1'
        co2data = [ele for ele in co2data if ele[i] == to_keep]

        
    oxydata = "".join(oxydata[0])
    co2data = "".join(co2data[0])

    print(int(oxydata, 2) * int(co2data, 2))
       