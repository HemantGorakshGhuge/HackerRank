# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
answer = []
for i in range(int(input())):
    B = set(map(int, input().split()))
    if B.intersection(A) == B:
        if len(B) < len(A):
            answer.append(True)
        else:
            answer.append(False)
    else:
        answer.append(False)

print(all(answer))
