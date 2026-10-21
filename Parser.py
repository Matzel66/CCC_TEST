def read_file(filename : str):
    with open(filename, 'r') as file:
        data = file.read()
        #print(data)
        lines = data.splitlines()

        N = int(lines[0])
        C = int(lines[1])
        Currency = lines[2:]

    ret_vals = {"N": N, "C": C, "Currency": Currency}
    print("N =", N)
    print("C =", C)
    print("Currencies =", Currency)
    return ret_vals 