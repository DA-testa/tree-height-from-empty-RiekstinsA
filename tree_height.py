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

    def max_height(node):
        if not adj_list[node]:
            return 1
        else:
            return 1 + max([max_height(child) for child in adj_list[node]])

    return max_height(root)


def main():
    inputstr = input().strip()
    inputval = inputstr.split('\\r\\n')

    if "I" in inputval:
        n = int(inputval[1])
        parents = list(map(int, inputval[2].split()))

    elif "F" in inputval:
        filename = inputstr.split('\\r\\n')[1]
        testfolder = "./test/" + filename

        with open (testfolder, mode = 'r') as file:
            text = file.read().strip()
            n, parents = int(text.split('\n')[0]), list(map(int, text.split('\n')[1].split()))

    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
