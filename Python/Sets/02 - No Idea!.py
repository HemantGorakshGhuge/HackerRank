# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
elements = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for element in elements:
    if element in A:
        happiness+=1
    if element in B:
        happiness-=1
print(happiness)
