# user=100
# for i in range(user):
#     user=user-1
#     print(i)
#     print(user)
# print("useruseruseruseruseruseruser",user)

# i=15
# j=1
# while j<i:
#     print("i",i)
#     print("j",j)
#     j+=1
#     i+=1

# word="radara"
# tempword=''
# for i in range(len(word),0,-1):
#     tempword=tempword+word[i-1]
#     print(tempword)

# def hash(char):
#     sum=0
#     for i in range(len(char)):
#         sum+=ord(char[i])*i
#     return sum
# print(hash("start"))
# print(hash("start"))
x=100
# def func(y):
#     y=900
#     x=y
#     return x
# print(func(x))
# print(x)
# print(5//2)
# print(5/2)

# a=[0,1,2,3,4,5,6,7]
# b=list(a[3:None])
# print(a)
# print(b)
# b.pop()
# print(a)
# print(b)

# Ford-Fulkerson algorith in Python




# from collections import defaultdict


# class Graph:

#     def __init__(self, graph):
#         self.graph = graph
#         self. ROW = len(graph)


#     # Using BFS as a searching algorithm 
#     def searching_algo_BFS(self, s, t, parent):

#         visited = [False] * (self.ROW)
#         queue = []

#         queue.append(s)
#         visited[s] = True

#         while queue:

#             u = queue.pop(0)

#             for ind, val in enumerate(self.graph[u]):
#                 if visited[ind] == False and val > 0:
#                     queue.append(ind)
#                     visited[ind] = True
#                     parent[ind] = u

#         return True if visited[t] else False

#     # Applying fordfulkerson algorithm
#     def ford_fulkerson(self, source, sink):
#         parent = [-1] * (self.ROW)
#         max_flow = 0

#         while self.searching_algo_BFS(source, sink, parent):

#             path_flow = float("Inf")
#             s = sink
#             while(s != source):
#                 path_flow = min(path_flow, self.graph[parent[s]][s])
#                 s = parent[s]

#             # Adding the path flows
#             max_flow += path_flow

#             # Updating the residual values of edges
#             v = sink
#             while(v != source):
#                 u = parent[v]
#                 self.graph[u][v] -= path_flow
#                 self.graph[v][u] += path_flow
#                 v = parent[v]

#         return max_flow


# graph = [[0, 8, 0, 0, 3, 0],
#          [0, 0, 9, 0, 0, 0],
#          [0, 0, 0, 0, 7, 2],
#          [0, 0, 0, 0, 0, 5],
#          [0, 0, 7, 4, 0, 0],
#          [0, 0, 0, 0, 0, 0]]

# g = Graph(graph)

# source = 0
# sink = 5

# print("Max Flow: %d " % g.ford_fulkerson(source, sink))


# temp = format(103, "b")
# print(temp)

# print(int("1101",2))

p="0ababaa" # 0 lagao start me
m=len(p)
arr=[]
for i in range(m+3):
    arr.append(0)
arr[1]=0
k=0
print(1,0)
for q in range(2,m):
    while k>0 and p[k+1]!=p[q]:
        k=arr[q]
    if p[k+1]==p[q]:
        k+=1
    arr[q]=k
    print(q,k)
