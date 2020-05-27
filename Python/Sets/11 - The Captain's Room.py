# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
room_numbers = list(map(int, input().split()))

captain_number = (K*sum(set(room_numbers))-sum(room_numbers))//(K-1)
print(captain_number)
