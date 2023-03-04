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
            # base case: leaf node
            return 1
        else:
            return 1 + max([height(child) for child in adj_list[node]])

    return height(root)

def main():

    input_string = input().strip()
    input_values = input_string.split('\\r\\n')
    n = int(input_values[1])
    parents = list(map(int, input_values[2].split()))

    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
