# python3

import sys
import threading


def compute_height(nodes, parents):

    adj_list = [[] for _ in range(nodes)]
    for i in range(nodes):
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
    input_i_f = input()

    if input_i_f == "I":
        nodes = int(input())
        parents = list(map(int, input().split()))

    elif input_i_f == "F":
        filename = input()
        if "a" in filename:
            print("invalid file name (a)")
            return
        try:
            testfolder = "./test/" + filename
            with open(testfolder, 'r') as f:
                nodes = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
        except FileNotFoundError:
            print("file not found")
            return
    else:
        print("invalid input type")
        return

    print(compute_height(nodes, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
