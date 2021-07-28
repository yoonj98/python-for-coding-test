# 이진 탐색 - 반복문 (190p)

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input("생성할 원소 개수 입력 : "))
target = int(input("찾고자 하는 원소 입력 : "))

arr = list(map(int, input("원소 입력 : ").split()))

if binary_search(arr, target, 0, n-1) == None:
    print("원소가 존재하지 않습니다.")
else:
    print(target,"은", binary_search(arr, target, 0, n-1)+1, "번째에 있습니다.")