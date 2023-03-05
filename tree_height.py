# python3

import sys
import threading
import numpy as np


def compute_height(node, parents):
    if node not in parents:
        return 1
    else:
        locs = np.where(parents == node)[0]
        return 1 + max(compute_height(i, parents) for i in locs)


def main():
    parents = np.array(list(map(int, input().split())))
    root = np.where(parents == -1)[0][0]
    print(compute_height(root, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

threading.Event().wait()
