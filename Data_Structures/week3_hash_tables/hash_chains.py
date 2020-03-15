# python3
import numpy as np

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = self._make_list(bucket_count)

    def _make_list(self, bucket_count):
        array = np.empty((bucket_count,),dtype=object)
        for i in range(len(array)):
            array[i] = [] 
        return array
    
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
            
        if query.type == "check":
            self.write_chain(self.elems[query.ind])
            
        else:
            ind_list = self.elems[self._hash_func(query.s)]
            if query.type =="add":
                for i in ind_list:
                    if i == query.s:
                        return
                ind_list.insert(0, query.s)
                    
            elif query.type == "del":
                try:
                    ind_list.remove(query.s)
                except ValueError:
                    pass 
                
            else:
                self.write_search_result(query.s in ind_list)
                
    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())



if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
