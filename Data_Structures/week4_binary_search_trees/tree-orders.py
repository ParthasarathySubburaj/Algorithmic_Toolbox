# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        self.inOrderTraversal(0)
        return self.result

    def inOrderTraversal(self, node):
        if node == -1:
            return
        self.inOrderTraversal(self.left[node])
        self.result.append(self.key[node])
        self.inOrderTraversal(self.right[node])
        
    def preOrder(self):
        self.result = []
        self.preOrderTraversal(0)
        return self.result
    
    def preOrderTraversal(self, node):
        if node == -1:
            return
        self.result.append(self.key[node])
        self.preOrderTraversal(self.left[node])
        self.preOrderTraversal(self.right[node])

    def postOrder(self):
        self.result = []
        self.postOrderTraversal(0)
        return self.result

        
    def postOrderTraversal(self, node):
        if node == -1:
            return
        self.postOrderTraversal(self.left[node])
        self.postOrderTraversal(self.right[node])
        self.result.append(self.key[node])

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
