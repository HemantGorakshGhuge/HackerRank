# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int, input().split()))
m = int(input())
for i in range(m):
    entries = input().split()
    command = entries[0]
    if command == 'intersection_update':
        B = set(map(int, input().split()))
        A.intersection_update(B)
    elif command == 'update':
        B = set(map(int, input().split()))
        A.update(B)
    elif command == 'symmetric_difference_update':
        B = set(map(int, input().split()))
        A.symmetric_difference_update(B)
    elif command == 'difference_update':
        B = set(map(int, input().split()))
        A.difference_update(B)

print(sum(A))
