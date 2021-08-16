# 정렬된 배열에서 특정 수의 개수 구하기 (367p)

# bisect : 배열 이진 분할 라이브러리 
# bisect_left(literable, value) : 왼쪽 인덱스를 구하기
# bisect_right(literable, value) : 오른쪽 인덱스를 구하기

from bisect import bisect_left, bisect_right

def cnt_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) 
array = list(map(int, input().split())) 
cnt = cnt_range(array, x, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)