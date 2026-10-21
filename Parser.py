def read_file(filename : str):
    with open(filename, 'r') as file:
        data = file.read()
        #print(data)
        lines = data.splitlines()
        currencies = []
        N = int(lines[0])
        C = int(lines[1])
        Currency = lines[2:]
        for line in Currency:
            line = line.split(' ')
            #line = map(int, line)
            relm = []
            for current in line:
                current = int(current)
                relm.append(current)
            currencies.append(relm)


    ret_vals = {"N": N, "C": C, "Currency": currencies}
    print("N =", N)
    print("C =", C)
    print("Currencies =", currencies)
    return ret_vals 
