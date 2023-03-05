#python3

import sys
import threading
import numpy as np


def compute_height(parents):
    max_height = 0
    heights = [0] * len(parents)
    for i in range(len(parents)):
        current = i
        height = 0
        while current != -1:
            if heights[current] != 0:
                height += heights[current]
                break
            height += 1
            current = parents[current]
        heights[i] = height
        max_height = max(max_height, height)
    return max_height




def main():
    parents = np.array(list(map(int, input().split())))
    print(compute_height(parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

threading.Event().wait()
