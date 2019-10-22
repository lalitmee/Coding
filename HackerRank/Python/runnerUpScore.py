if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_array = sorted(arr, reverse=True)
    unique_numbers = sorted(list(set(sorted_array)), reverse=True)
    print(unique_numbers[1])

