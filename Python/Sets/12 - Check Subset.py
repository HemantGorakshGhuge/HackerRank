# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    A_size = int(input())
    A = set(map(int, input().split()))
    B_size = int(input())
    B = set(map(int, input().split()))
    new_set = A.intersection(B)
    print(new_set == A)
