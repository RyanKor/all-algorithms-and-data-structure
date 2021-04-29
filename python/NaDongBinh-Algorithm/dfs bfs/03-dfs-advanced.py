# 깊이 우선 탐색, 스택을 사용한다.
def dfs(graph, v, visited):
    visited[v] = True # 매개변수 v 노드값이 현재 위치이므로 방문한 상태로 변경한다.
    print(v, end=" ")
    for i in graph[v]: # 현재 노드에서 연결된 다른 노드 값들을 재귀 함수 형태로 호출하면서 방문
        if not visited[i]: # 연결된 노드를 아직 방문하지 않았다면 재귀 함수 형태로 방문한다.
            dfs(graph, i, visited)

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

dfs(graph,1,visited)