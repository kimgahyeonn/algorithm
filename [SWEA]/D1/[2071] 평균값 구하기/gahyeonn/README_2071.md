# 2071. 평균값 구하기 #

10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라. (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

**[제약 사항]**

각 수는 0 이상 10000 이하의 정수이다.

**[입력]**

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다. 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

**[출력]**

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```
T = int(input())
for test_case in range(1, T + 1):
    val = input().split(' ')
    int_val = list(map(int, val))
    sum = 0
    ave = 0

    for num in int_val :
        sum += num
        ave = sum / len(int_val)

    print(f'#{test_case} {round(ave)}')
```

- input할 때 split를 활용하여 공백으로 문자를 구분
- int_val에 list와 map 활용하여 int 타입으로 리스트에 저장
- sum 변수에 int_val의 각 값을 num으로 접근하여 하나씩 더함
- ave에 평균값을 구한 후, print에 round를 통하여 소수점 반올림