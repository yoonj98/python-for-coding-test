# 문자열 압축 (323p)

def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:i] # 앞에서부터 문자열 추출
        count = 1
        
        for j in range(i, len(s), i):
            if prev == s[j:j + i]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + i] # 다시 상태 초기화
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer