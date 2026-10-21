from Parser import read_file

if __name__ == "__main__":
    filename = "Angaben/level-1/in_level-1_1-small.txt"
    result = read_file(filename)
    processing = result['Currency']
    for currency in processing:
        n = 0 
        while True:
            if n not in currency:
                n = n + 1
            else:
                break
        print(n)

        