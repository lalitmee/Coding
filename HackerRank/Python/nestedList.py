if __name__ == '__main__':
    array = []
    scores_array = []
    for _ in range(int(input())):
        name_score_dict = dict()
        name = input()
        score = float(input())
        scores_array.append(score)
        name_score_dict['name'] = name
        name_score_dict['score'] = score
        array.append(name_score_dict)

    unique_scores = sorted(list(set(scores_array)))
    second_lowest_score = unique_scores[len(unique_scores)- 2]
    names_array = []
    for obj in array:
        if obj["score"] == second_lowest_score:
            names_array.append(obj["name"])

    sorted_names_array = sorted(names_array)
    for name in sorted_names_array:
        print(name)
