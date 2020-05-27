# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
cities = set()
for i in range(n):
    cities.add(input())

print(len(cities))
