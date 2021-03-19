from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """
        type root : TreeNode
        rtype: str
        """
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                queue.extend([node.left, node.right])
                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)
    
    def deserialize(self, data):
        '''
        type data: str
        rtype: TreeNode
        '''
        if data == '#':
            return None
        
        nodes = deque(data.split())

        root = TreeNode(int(nodes.popleft()))
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                l, r = nodes.popleft(), nodes.popleft()
                node.left = TreeNode(int(l)) if l != "#" else None
                node.right = TreeNode(int(r)) if r != "#" else None
                queue.extend([node.left, node.right])
        return root

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.left = TreeNode(5)

    serializer = Codec()
    deserializer = Codec()

    print(serializer.serialize(root))
    print(deserializer.deserialize(serializer.serialize(root)))