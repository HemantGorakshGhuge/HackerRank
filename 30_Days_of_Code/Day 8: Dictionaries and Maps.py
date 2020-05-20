import sys

input_list = []

for line in sys.stdin:
    input_list.append(line)

n = int(input_list[0])
entries = input_list[1:n+1]
queries = input_list[n+1:]

dictionary = dict()

for entry in entries:
    name, number = entry.split()
    dictionary[name] = number

for query in queries:
    input_name = query.rstrip() #Removes whitespace and newline
    if input_name in dictionary:
        print(input_name+'='+dictionary[input_name])
    else:
        print('Not found')
