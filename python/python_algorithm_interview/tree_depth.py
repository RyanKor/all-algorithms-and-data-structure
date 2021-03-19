from collections import deque
class TreeNode:
    # 이진트리 정의
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root : TreeNode) -> int:
        if root is None:
            return 0
        queue = deque([root])
        depth = 0

        while queue:
            depth +=1

            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth
TreeNode([3,9,20,None, None, 15,7])
print(Solution([3,9,20,None, None, 15,7]))