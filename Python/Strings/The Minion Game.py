def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    string = list(string)

    Stuart_Score = 0
    Kevin_Score = 0

    for i in range(len(string)):
        if string[i] in vowels:
            Kevin_Score += len(string) - i
        else:
            Stuart_Score += len(string) - i

    if Stuart_Score > Kevin_Score:
        print("Stuart", Stuart_Score)
    elif Stuart_Score < Kevin_Score:
        print("Kevin", Kevin_Score)
    else:
        print("Draw")
