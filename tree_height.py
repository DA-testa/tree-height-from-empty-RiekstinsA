# python3

import sys
import threading


def compute_height(n, parents):

    adj_list = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            adj_list[parent].append(i)

    def height(node):
        if not adj_list[node]:
            return 1
        else:
            return 1 + max([height(child) for child in adj_list[node]])

    return height(root)


def main():
    
    input_string = input().strip().split('\n') + input().strip().split('\r')
    n = int(input_string[1])
    parents = list(map(int, input_string[2].split()))
    
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
