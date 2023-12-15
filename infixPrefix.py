class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.num = 0

    def insert(self, cur: Node, data: int):
        if self.root is None:
            self.root = Node(data)
            self.num += 1
            return self.root
        
        if cur.data == data:
            return self.root
        
        if cur.data < data:
            if cur.right is not None:
                self.insert(cur.right, data)
            else:
                cur.right = Node(data)
                self.num += 1
        else:
            if cur.left is not None:
                self.insert(cur.left, data)
            else:
                cur.left = Node(data)
                self.num += 1
        
        return self.root

    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def preorder(self, node: Node, q: list) -> list:
        if node is None:
            return []
        
        q.append(str(node.data))
        q += self.preorder(node.left, [])
        q += self.preorder(node.right, [])

        return q

    def inorder(self, node: Node) -> str:
        if node is None:
            return []

        if node.left is None and node.right is None:
            return str(node.data)
        
        return '(' + self.inorder(node.left) + str(node.data) + self.inorder(node.right) + ')'

inp = input('Enter Postfix : ')
print('Tree :')

S = []

for ch in inp:
    n = Node(ch)
    if ch in '+-*/':
        if len(S) >= 2:
            n.right = S.pop(-1)
            n.left = S.pop(-1)
            S.append(n)
    else:
        S.append(n)
        

T = BST()
T.root = S[0]
T.printTree(T.root)
print('--------------------------------------------------')
print(f'Infix : {T.inorder(T.root)}')
print(f'Prefix : {"".join(T.preorder(T.root, []))}')