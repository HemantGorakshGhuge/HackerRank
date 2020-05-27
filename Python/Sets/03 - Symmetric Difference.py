# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input()
m_set = set(map(int, input().split()))
n = input()
n_set = set(map(int, input().split()))
symmetric = sorted(m_set.symmetric_difference(n_set))
for element in symmetric:
    print(element)
