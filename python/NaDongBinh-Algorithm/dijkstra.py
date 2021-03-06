import sys
import heapq

INF = int(1e9) # 무한을 의미하는 수로 10억 설정, sys.maxsize 사용 가능

# 노드 개수, 간선의 갯수를 입력받기
N,M = map(int,input().split())

# 시작 노드 번호 받기
start=int(input())
graph = [[]for i in range(N+1)] # 각 노드에 연결되어 있는 정보를 담는 리스트 생성

distance = [INF] * (N+1) # 최단 거리 테이블을 모두 거리 무한대로 초기화

for _ in range(M):
    a,b,c = map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 C라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입한다.
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,N+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

'''
입력 예시
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''