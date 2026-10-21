from Parser import read_file

def ret_max_val(in_arr : list):
    max_val = 0
    for i in in_arr:
        if int(i) > max_val:
            max_val = int(i)
    return max_val


def process_withdrawal(coins, wanting):
    '''
    coins = list of possible coin values
    wanting = list of wanted coin values

    - returns the constilation to make the wanted value with the smalest amount of coins possible
    - if not possible returns -1
    '''
    coin_values = sorted({int(coin) for coin in coins if int(coin) > 0})
    withdrawals = []

    for wanted in wanting:
        amount = int(wanted)
        if amount < 0:
            withdrawals.append(-1)
            continue

        
        minimum = [float("inf")] * (amount + 1)
        last_coin = [None] * (amount + 1)
        minimum[0] = 0

        for value in range(1, amount + 1):
            for coin in coin_values:
                if coin > value:
                    break
                if minimum[value - coin] + 1 < minimum[value]:
                    minimum[value] = minimum[value - coin] + 1
                    last_coin[value] = coin

        if minimum[amount] == float("inf"):
            withdrawals.append(-1)
            continue

        combination = []
        value = amount
        while value:
            coin = last_coin[value]
            combination.append(coin)
            value = value - coin
        withdrawals.append(combination)

    return withdrawals



if __name__ == "__main__":
    filename = "Angaben/level-1/in_level-1_5-large.txt"
    result = read_file(filename)
    spone = []
    sptwo = []
    for i, line in enumerate(result["Currency"]):
        if i % 2 == 0:
            spone.append(line)
        else:
            sptwo.append(line)
    