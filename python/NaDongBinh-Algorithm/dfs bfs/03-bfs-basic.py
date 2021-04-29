from collections import deque

def bfs(graph, start,visited):
    queue = deque([start]) #deque를 사용해 큐 기능 구현
    visited[start] = True # 방문한 지점은 모두 True로 변경
    while queue: # 큐가 멈추면 끝
        v = queue.popleft() # queue에서 방문한 지점은 빼낸다.
        print(v,end=" ")
        for i in graph[v]: # 현재 v 노드에 연결된 지점을 탐색하되
            if not visited[i]: # 방문하지 않은 곳이라면
                queue.append(i) # 큐에 넣고
                visited[i] = True # 모두 방문한 것으로 변경한다.

graph = [
    [], # 0번째 노드는 인덱싱을 위해 삽입
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * len(graph)

bfs(graph,1,visited)