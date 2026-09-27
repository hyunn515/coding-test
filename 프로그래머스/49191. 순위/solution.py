from collections import defaultdict

def solution(n, results):
    wins = defaultdict(list)
    loses = defaultdict(list)
    
    for a, b in results:
        wins[a].append(b)
        loses[b].append(a)
    
    def dfs(k, g):
        visited = [False] * (n + 1)
        visited[k] = True
        stack = [k]
        count = 0
        
        while stack:
            s = stack.pop()
            
            for nxt in g[s]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)
                    count += 1
        
        return count
    
    ans = 0
    for i in range(1, n + 1):
        win = dfs(i, wins)
        lose = dfs(i, loses)
        
        if win + lose == n - 1:
            ans += 1
            
    return ans
        
