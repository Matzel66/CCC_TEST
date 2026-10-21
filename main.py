from Parser import read_file

def ret_max_val(in_arr : list):
    max_val = 0
    for i in in_arr:
        if int(i) > max_val:
            max_val = int(i)
    return max_val


if __name__ == "__main__":
    filename = "Angaben/level-1/in_level-1_5-large.txt"
    result = read_file(filename)
    processing = result['Currency']
    for currency in processing:
        print("Currency =", currency)
        n = 1
        while n < ret_max_val(currency):
            if n not in currency:
                break
            else:
                n += 1
        with open(f"{filename}.out", 'a') as file:
            file.write(f"{n}\n")

        