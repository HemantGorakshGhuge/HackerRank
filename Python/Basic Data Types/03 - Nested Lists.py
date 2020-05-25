if __name__ == '__main__':
    python_students = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
        scores.add(score)

    sorted_scores = sorted(scores)
    second_lowest_score = sorted_scores[1]
    # print(python_students)
    # print(sorted_scores)
    # print(second_lowest_score)
    
    name_list = []
    for student in python_students:
        name = student[0]
        score = student[1]
        if score == second_lowest_score:
            name_list.append(name)
    
    sorted_name_list = sorted(name_list)
    for name in sorted_name_list:
        print(name)
