
def processing(value, coins):
    for c in coins:
        result = value - c
        print(result)
        if result in coins:
            return [c, value-c]

print(processing(10, [1, 2, 5]))
        