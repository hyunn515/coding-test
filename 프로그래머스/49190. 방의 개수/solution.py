def solution(arrows):
    directions = ((-1, 0), (-1, 1), (0, 1), (1, 1),(1, 0), (1, -1), (0, -1), (-1, -1))
    
    cur = (0, 0)
    visited_points = {cur}
    visited_edges = set()
    ans = 0
    
    for arrow in arrows:
        dr, dc = directions[arrow]
        
        for _ in range(2):
            nxt = (cur[0]+dr, cur[1]+dc)
            edge = tuple(sorted((cur, nxt)))
            if nxt in visited_points and edge not in visited_edges:
                ans += 1
            
            visited_points.add(nxt)
            visited_edges.add(edge)
            cur = nxt
    
    return ans
            
    
