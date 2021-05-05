import heapq

# 결과 --> 런타임 에러 & 시간 초과 : 더 빠른 연산을 필요로 한다.
# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville)

#     while min(scoville) < K:
#         first = heapq.heappop(scoville)
#         second = heapq.heappop(scoville)
#         if first + (second * 2) < K:
#             satisfaction = first + (second * 2)
#             heapq.heappush(scoville, satisfaction)
#             answer +=1
#         elif first + (second * 2) >= K:
#             satisfaction = first + (second * 2)
#             heapq.heappush(scoville, satisfaction)
#             answer +=1            
#             pass
#         else:
#             return -1
#     return answer

# 결과 -> 정답
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville)> 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            answer +=1         
        else:
            return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12]	, 7))