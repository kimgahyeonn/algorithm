# 병합 정렬

리스트를 반으로 쪼개고 그 반을 또 쪼개는 것을 반복하여 요소가 한 개뿐인 리스트로만 남았을 때 병합

### 1. 다 쪼개기
`[6, 3, 9, 2]`
반으로 쪼개면 `[6, 3], [9, 2]`
또 쪼개면 `[6], [3], [9], [2]`

### 2. 하나씩 병합하기
`[3, 6], [2, 9]`
- 먼저 [6]과 [3]을 병합하고 다음으로 [9]와 [2]를 병합
- 각 리스트에 숫자 한 개만 있었으므로 서로 비교 후 더 작은 숫자를 리스트의 처음 위치에 둠

### 3. 두 리스트 병합하기
`[]`

### 4. 두 리스트 비교하기
병합 전 `[3, 6], [9]` 후 `[2]`
- 두 리스트의 첫 번째 요소인 3과 2 비교하여 더 작은 2가 **새로운 병합 리스트**에 들어감

### 5. 두 리스트 비교하기2
병합 전 `[6], [9]` 후 `[2, 3]`
- 3과 9를 비교하여 3이 더 작으므로 병합 리스트에 추가

### 6. 두 리스트 비교하기3
병합 전 `[], []` 후 `[2, 3, 6, 9]`
- 6이 더 작으므로 병합 리스트에 추가, 마지막 남은 9도 추가

## 코드로 알아보기
```py
def merge_sort(a_list) :
# a_list, left_half, right_half 총 3개의 변수 생성
    if len(a_list) > 1 : # 리스트의 길이가 2 이상이어서 쪼갤 것이 있다면

        mid = len(a_list) # mid에 총 리스트의 길이가 할당
        left_half = a_list[:mid] # 리스트의 절반만큼 왼쪽 서브리스트
        right_half = a_list[:mid] #리스트의 절반만큼 오른쪽 서브리스트

        merge_sort(left_half) # 재귀. _half를 배개변수로 전달하며 다시 재귀
        merge_sort(right_half) # 재귀
        # 리스트를 서브 리스트로 분할. 계속 쪼갬

        left_ind = 0
        right_ind = 0
        alist_ind = 0
        # 리스트의 인덱스번호를 모두 0으로

        while left_ind < len(left_half) and right_ind < len(right_half)
        # 왼쪽 리스트의 인덱스번호가 반으로 쪼갠 리스트보다 작은 동안 (리스트를 초과하지 않는다면)

            if left_half[left_ind] <= right_half[right_ind] :
            # 왼쪽 인덱스가 오른쪽 인덱스보다 작거나 같다면,
            a_list[alist_ind] = left_half[right_ind]
            left_ind += 1
            # 새로운 병합 리스트에 왼쪽 값 추가

            else :
            a.list[alist_ind] = right_halp[right_ind]
            # 새로운 병합 리스트와 오른쪽 인덱스와 같다면
            right_ind += 1
            # 오른쪽 인덱스 값이 1 증가하여 옆자리 가리키게 함
        alist_ind += 1
        # while문이 한 번 순회하면 새 병합 리스트가 가리키는 인덱스 값도 증가하게 함

    while left_ind < len(left_half) :
    # 왼쪽 값의 인덱스 번호가 왼쪽 리스트의 길이보다 작으면 정렬해야할 일이 남았다는 뜻

        a_list[alist_ind] = left_half[left_ind]
        left_ind += 1
        alist_ind += 1
        # 왼쪽 인덱스 값를 병합 인덱스에 추가하고 둘 다 인덱스번호 증가시킴

    while right_ind < len(right_half) :
    # 오른쪽 값의 인덱스 번호가 오른쪽 리스트의 길이보다 작으면 정렬해야 할일이 남았다는 뜻

        a_list[alist_ind] = right_half[right_ind]
        right_ind += 1
        alist_ind += 1
        # 오른쪽 인덱스 값를 병합 인덱스에 추가하고 둘 다 인덱스번호 증가시킴    
        # 오른쪽 인덱스 값을 처리한 것과 동일

## 병합 정렬의 사용
    - O(nlogn)
    - 50명의 학생이 있는 반에서 돈을 걷을 때, 선생이 나서서 걷지 않고 각자가 가지고 있는 돈을 학생들이 직접 합칠 때. 자신의 뒤에 있는 학생에게 돈을 받아 자신이 갖고 있는 돈과 합쳐서 단 한명의 학생이 남을 때까지 반복하는 것
