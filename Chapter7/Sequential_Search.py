# 순차탐색 (187p)

def sequential_search(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i+1

n = int(input("생성할 원소 개수 입력 : "))
target = input("찾고자 하는 원소 입력 : ")

arr = input("원소 입력 : ").split()
print(target,"은", sequential_search(n, target, arr), "번째에 있습니다.")