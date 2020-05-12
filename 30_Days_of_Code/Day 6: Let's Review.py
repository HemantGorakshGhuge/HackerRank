# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    S = input()
    S_odd = ""
    S_even = ""
    for i in range(len(S)):
        if i%2: #Odd
            S_odd += S[i]
        else:   #Even
            S_even += S[i]
    print(S_even, S_odd)
