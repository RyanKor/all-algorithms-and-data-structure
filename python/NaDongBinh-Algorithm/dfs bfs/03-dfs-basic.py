# 나동빈의 파이썬 알고리즘 인터뷰 기반 작성

# 그래프의 구조 : Node, Edge, Vertex
import sys
INF = sys.maxsize
# 인접 행렬 방식
graph = [ # 0, 1, 2 라는 3개의 노드에 대해
    [0, 7, 5], # 0번 노드는 1에는 7이라는 edge값이, 2에는 5라는 edge값이 연결되어 있음을 확인
    [7, 0 , INF], # 1번 노드는 0에 7, 2에 연결이 안되어 있음
    [5, INF, 0] # 2번 노드는 0에 5, 1에 연결 안되어 있음
]

# 인접 리스트 방식
# 메모리 효율성은 인접 리스트가 더 높다 (불필요한 노드 정보를 삭제하기 때문)
# 그러나 두 노드가 연결되어 있는지에 대한 정보를 체크하는 것이 느리다.
# 특정 노드와 연결된 모든 인접 노드를 순회할 때는 인접 리스트가 행렬 방식에 비해 효율이 좋다.
adjacent_list = [[] for _ in range(3)]

adjacent_list[0].append((1,7))
adjacent_list[0].append((2,5))

adjacent_list[1].append((0,7))

adjacent_list[2].append((0,5))