def solution(distance, rocks, n):
    ab = sorted([0] + rocks + [distance])
    
    l, r = 1, distance
    ans = 0
    
    while l <= r:
        gap = (l + r) // 2
        removed = 0
        a = 0
        
        for b in ab[1:]:
            if b - a < gap:
                removed += 1
            else:
                a = b
        
        if removed <= n:
            ans = gap
            l = gap + 1
        else:
            r = gap - 1
    
    return ans
