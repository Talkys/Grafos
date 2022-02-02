# Python 3 program to convert Adjacency matrix
# representation to Adjacency List

from collections import defaultdict


# converts from adjacency matrix to adjacency list
def convert(matrix):
    adj_list = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    return adj_list


# driver code
a = [[0, 1, 1], [0, 0, 1], [1, 1, 0]]  # adjacency matrix
AdjList = convert(a)
print("Adjacency List:")
# print the adjacency list
for i in AdjList:
    print(i, end="")
    for j in AdjList[i]:
        print(" -> {}".format(j), end="")
    print()
