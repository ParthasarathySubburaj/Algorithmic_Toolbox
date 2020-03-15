#!/usr/bin/python3

import sys, threading
import numpy as np

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class BstTree:
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
    
    def inOrderTraversalCheck(self,node, ll, ul):
        if node == -1:
            return True
        if (self.key[node] < ul and self.key[node] > ll):
            return (self.inOrderTraversalCheck(self.left[node],ll, self.key[node]) \
                    and self.inOrderTraversalCheck(self.right[node], self.key[node], ul))
        else:
            return False
        
    def isBST(self):
        if self.n == 0:
            return True
        return self.inOrderTraversalCheck(0,-np.inf, np.inf)
    


def main():
    tree = BstTree()
    tree.read()
    if tree.isBST():
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
