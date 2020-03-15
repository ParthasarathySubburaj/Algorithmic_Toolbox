#python3
import sys

import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max = -1000000
        self.__max_list = []
        
    def Push(self, a):
        self.__stack.append(a)
        if a>=self.__max:
            self.__max = a
            self.__max_list.append(a)
            
    def Pop(self):
        assert(len(self.__stack))
        poped_value = self.__stack.pop()
        if poped_value == self.__max:
            self.__max_list.pop()
            self.__max = self.__max_list[-1]

    def Max(self):
        assert(len(self.__stack))
        return self.__max


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
