if __name__ == '__main__':
    N = int(input())
    array = []
    for _ in range(N):
        line = list(input().rstrip().split())
        if line[0] == 'insert':
            position = int(line[1])
            element = int(line[2])
            array.insert(position, element)
        elif line[0] == 'print':
            print(array)
        elif line[0] == 'remove':
            array.remove(int(line[1]))
        elif line[0] == 'append':
            array.append(int(line[1]))
        elif line[0] == 'sort':
            array = sorted(array)
        elif line[0] == 'pop':
            array.pop()
        elif line[0] == 'reverse':
            new_array = []
            for i in range(len(array)):
                new_array.append(array[len(array)-i-1])
            array = new_array
