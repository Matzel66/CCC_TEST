infile = input("Enter the input file name: ")

with open (infile, 'r') as file:
    data = file.read()
    #print(data)
    lines = data.splitlines()

    N = int(lines[0])
    C = int(lines[1])
    Currency = lines[2:]


print("N =", N)
print("C =", C)
print("Currency =", Currency)