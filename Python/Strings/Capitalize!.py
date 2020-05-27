# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    print(s)
    word_list = []
    for word in s:
        word_list.append(word.capitalize())
    string = " "
    print(word_list)
    string = string.join(word_list)
    return string

