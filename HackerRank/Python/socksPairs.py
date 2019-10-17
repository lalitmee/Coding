# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    unique_socks_list = list(set(ar))
    socks_frequencies = dict()
    for sock in range(len(unique_socks_list)):
        count = 0
        for s in ar:
            if s == unique_socks_list[sock]:
                count += 1
                socks_frequencies[s] = count
    sum = 0
    for value in socks_frequencies.values():
        sum += value // 2

    return sum


socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(1, socks))
