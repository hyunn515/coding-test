def solution(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    for i, m in enumerate(money[1:], 1):
        dp1[i] = max(dp1[i - 1], dp1[i -2] + m)
    for i, m in enumerate(money[:-1], 1):
        dp2[i] = max(dp2[i - 1], dp2[i -2] + m)
    return max(dp1[-1], dp2[-1])

        
        
    
    
