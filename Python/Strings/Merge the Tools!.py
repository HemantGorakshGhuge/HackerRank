def merge_the_tools(string, k):
    # your code goes here
    string = list(string)
    # print(string)
    num_segments = int(len(string)/k)
    # print(num_segments)
    t = []
    for i in range(num_segments):
        t.append(string[i*k:k*(i+1)])
    # print(t)
    u = set()
    for t_n in t:
        u_element = ''
        for i in t_n:
            if i in u_element:
                continue
            u_element += i
        print(u_element)
