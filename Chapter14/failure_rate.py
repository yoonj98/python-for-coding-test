# 실패율 (361p)

def solution(N, stages):
    res = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        res.append((i, fail))
        length -= count

    res = sorted(res, key=lambda x: x[1], reverse=True)   # 내림차순
    
    res = [i[0] for i in res]
    return res