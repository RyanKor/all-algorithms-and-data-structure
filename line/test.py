

def solution(table, languages, preference): # table -> list / language -> list / preference -> list
    answer = []
    table_dic = {}
    idx = ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]
    score_dic = {"SI": 0, "CONTENTS": 0, "HARDWARE": 0, "PORTAL": 0, "GAME": 0}
    for tb in table:
        table_dic[tb.split(' ')[0]] = tb.split(' ')[1:]
    for search in idx:
        for lang in languages:
            if lang in table_dic[search]:
                score_dic[search] += (5-table_dic[search].index(lang)) * preference[languages.index(lang)]
    for key, value in score_dic.items():
        if max(score_dic.values()) == value:
            answer.append(key)
    answer.sort()
    return answer[0]