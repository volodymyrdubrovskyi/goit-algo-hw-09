import timeit

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(sum_: int):
    count_coins = {}
    for coin in coins:
        count = sum_ // coin
        if count > 0:
            count_coins[coin] = count
        sum_ = sum_ - count * coin
    return count_coins

def find_min_coins(sum_ :int):
    min_coins_required = [0] + [float('inf')] * sum_
    last_coin_used = [0] * (sum_ + 1)
    for s in range(1, sum_ + 1):
        for coin in coins:
            if (s >= coin) and (min_coins_required[s-coin]+1 < min_coins_required[s]):
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin

    count_coins = {}
    current_sum = sum_
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum = current_sum - coin

    return count_coins


def main():
    result = find_coins_greedy(113)
    print('1. Жадібний алгоритм для суми 113: ', result)

    result = find_min_coins(113)
    print('2. Алгоритм динамічного програмування для суми 113: ', result)
    
    #test_group = [113, 226, 452, 904, 1808, 3616, 7232]
    test_group = [19, 24, 30, 36, 42, 48, 54]
    time_greedy = []
    time_min = []

    for i in range(0, len(test_group)):
        time_greedy.append(timeit.timeit(lambda: find_coins_greedy(test_group[i]), number=1000))
        time_min.append(timeit.timeit(lambda: find_min_coins(test_group[i]), number=1000))

    print('\nРезультати тестових прогонів:')
    print('Жадібний алгоритм, час для сум ', test_group,' (1000 повторів): \n', time_greedy)
    print('Алгоритм динамічного програмування, час для сум ', test_group,' (1000 повторів): \n', time_min)

    # пошук "хибного рішення" жадібного алгоритму
    print('пошук "хибного рішення" стартував....')
    for i in range(1, 5000):
        result_greedy = find_coins_greedy(i)
        result_min = find_min_coins(i)
        if i % 777 == 0:
            print(i, result_greedy, result_min)
        if result_greedy != result_min:
            print('Розбіжність: ', i, result_greedy, result_min)
    print('пошук "хибного рішення" завершен')

if __name__ == '__main__':
    main()