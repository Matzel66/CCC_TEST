from Parser import read_file

def ret_max_val(in_arr : list):
    max_val = 0
    for i in in_arr:
        if int(i) > max_val:
            max_val = int(i)
    return max_val


def process_withdrawal(coins, wanting):
    




if __name__ == "__main__":
    filename = "Angaben/level-2/in_level-2_0-example.txt"
    result = read_file(filename)
    spone = []
    sptwo = []
    for i, line in enumerate(result["Currency"]):
        if i % 2 == 0:
            spone.append(line)
        else:
            sptwo.append(line)
    