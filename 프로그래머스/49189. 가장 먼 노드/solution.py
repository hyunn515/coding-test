from collections import defaultdict, deque

def solution(n, edge):
    g = defaultdict(list)
    
    for a, b in edge:
        g[a].append(b)
        g[b].append(a)
        
    d = [-1] * (n  + 1)
    d[1] = 0
    q = deque([1])
    
    while q:
        x = q.popleft()
        for y in g[x]:
            if d[y] == -1:
                d[y] = d[x] + 1
                q.append(y)
    
    return d[1:].count(max(d[1:]))
