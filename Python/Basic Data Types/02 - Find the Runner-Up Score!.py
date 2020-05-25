if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = sorted(arr, reverse=True)
    maximum = arr[0]
    while arr[0] == maximum:
        arr.remove(maximum)
    print(arr[0])
