# [2070] 큰 놈, 작은 놈, 같은 놈 #

2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

**[제약 사항]**

각 수는 0 이상 10000 이하의 정수이다.

**[입력]**

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다. 각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.

**[출력]**

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```
T = int(input())

for test_case in range(1, T + 1):
    my_list = []

    num1, num2 = map(int, input().split())

    if num1 > num2 : print(f'#{test_case} >')
    elif num1 < num2 : print(f'#{test_case} <')
    else : print(f'#{test_case} =')

```

- 숫자 2개를 num1, num2에 각각 input함
- map 함수를 통하여 각각 int 형태로 저장
- 두 수를 비교하는 if문 수행