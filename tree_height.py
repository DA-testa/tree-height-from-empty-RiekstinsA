# python3

import sys
import threading

def compute_height(n, parents):
    if n == 0:
        return 0

    depths = [0] * n

    root = None
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            depths[i] = depths[parents[i]] + 1

    max_depth = max(depths)
    return max_depth

def main():
    input_string = input().strip()
    input_values = input_string.split('\\r\\n')
    
    # Check if input has correct format
    if len(input_values) < 2:
        print("Error: input is not well-formed")
        return
    
    if input_values[0] == "I":
        if len(input_values) < 3:
            print("Error: input is not well-formed")
            return
        n = int(input_values[1])
        parents = list(map(int, input_values[2].split()))
    elif input_values[0] == "F":
        if len(input_values) < 2:
            print("Error: input is not well-formed")
            return
        filename = input_values[1]
        testfolder = "./test/" + filename
        
        with open(testfolder, mode='r') as file:
            text = file.read().strip()
            n, parents = int(text.split('\n')[0]), list(map(int, text.split('\n')[1].split()))
    else:
        print("Error: invalid input")
        return
    
    sys.setrecursionlimit(10**7)
    height = compute_height(n, parents)
    print(height)
    
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
