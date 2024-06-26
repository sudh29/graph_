class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # DFS
        # visited = [False] * V
        # stack = []
    
        # def dfs(node):
        #     visited[node] = True
        #     for neighbor in adj[node]:
        #         if not visited[neighbor]:
        #             dfs(neighbor)
        #     stack.append(node)
        
        # for i in range(V):
        #     if not visited[i]:
        #         dfs(i)
        # return stack[::-1]
        
        # BFS
        val = [0 for i in range(V)]
        res = []
        q = []
        for i in range(V):
            for j in adj[i]:
                val[j]+=1
        for i in range(V):
            if val[i]==0: q.append(i)
        while len(q)!=0:
            data = q.pop(0)
            res.append(data)
            for j in adj[data]:
                val[j]-=1
                if val[j]==0: q.append(j)
        return res
        

#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
