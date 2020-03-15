# python3

import sys, threading
from collections import deque

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:

        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.tree, self.root_node = self.construct_tree(self.parent)
                
        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                queue = deque()
                queue.extend(self.tree[self.root_node])
                maxHeight = maxHeight+1
                target = queue[-1]
                
                while queue:
                    next_node = queue.popleft()
                    if next_node == target:
                        queue.extend(self.tree[next_node])
                        maxHeight = maxHeight + 1
                        if len(queue)>0:
                            target = queue[-1]
                    else:
                        queue.extend(self.tree[next_node])
                return maxHeight
                
        def construct_tree(self, parents):
            tree = [[] for count in range(self.n)]
            root_node = 0
            for child_node, parent_node  in enumerate(parents):
                if parent_node == -1:
                    root_node = child_node
                else:
                    tree[parent_node].append(child_node) 
            return tree, root_node
                    
def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
