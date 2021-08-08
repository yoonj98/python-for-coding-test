# 괄호 변환 (346p)

def balanced_index(p):
    cnt = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

def check_proper(p):
    cnt = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0: 
                return False
            cnt -= 1
    return True 

def solution(p):
    res = ''
    if p == '':
        return res
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    
    if check_proper(u):
        res = u + solution(v)
    else:
        res = '('
        res += solution(v)
        res += ')'
        u = list(u[1:-1]) # 인덱싱을 통해 처음과 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        res += "".join(u)
    return res