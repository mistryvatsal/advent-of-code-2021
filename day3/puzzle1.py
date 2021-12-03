files = ["sample_input.txt", "input.txt"]
for file in files:
    with open(file) as f:
        data = [d.rstrip() for d in f.readlines()]

    data = [list(d) for d in data]
    n = len(data[0])
    
    gamma_rate = []
    epsilon_rate = []

    for i in range(n):
        temp = []
        for bin in data:
            temp.append(bin[i])
        if temp.count('1') > temp.count('0'):
            gamma_rate.append('1')
        else:
            gamma_rate.append('0')
    
    # Calculating complement of gamma_rate
    epsilon_rate = ['1' if x == '0' else '0' for x in gamma_rate]
    
    gamma_rate = ''.join(gamma_rate)
    epsilon_rate = ''.join(epsilon_rate)
    
    print(int(gamma_rate, 2) * int(epsilon_rate, 2))