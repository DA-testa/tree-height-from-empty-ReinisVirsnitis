#python3

import sys
import threading
import numpy as np


def compute_height(node, parents, heights):
    if node not in parents:
        return 1
    elif heights[node] != -1:
        return heights[node]
    else:
        locs = np.where(parents == node)[0]
        heights[node] = 1 + max(compute_height(i, parents, heights)for i in locs)
        return heights[node]




def main():
    try:
        file_input = input()
        if file_input == "I":
            node = int(input())
            parents = np.array(list(map(int, input().split())))
        elif file_input == "F":
            file_name = input()
            if 'a' in file_name:
                raise ValueError
            with open("test/01", 'r', encoding = "utf-8") as file:
                node = int(file.readline())
                parents_str = file.readline().split()
                parents = np.array([int(x) for x in parents_str if x != ''])
        else:
            raise ValueError
        
        heights = np.full(node, -1)
        root = np.where(parents == -1)[0][0]
        print(compute_height(root, parents, heights))

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except IOError as e:
        print(f"Error: {e}")
        sys.exit(1)

    



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

threading.Event().wait()
