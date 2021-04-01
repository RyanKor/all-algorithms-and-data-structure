def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    # for idx, val in enumerate(citations, start=1):
    #     if idx <= val:
    #         answer.append(idx)
    answer = max(map(min, enumerate(citations, start=1)))       
    return answer