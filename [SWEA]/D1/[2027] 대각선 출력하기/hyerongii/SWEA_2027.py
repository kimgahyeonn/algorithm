'''
2027. 대각선 출력하기

주어진 텍스트를 그대로 출력하세요

#++++ 0 
+#+++ 1
++#++ 2 
+++#+ 3
++++# 4
'''


# 플러스 5개로 이루어진 곳에 인덱스 증가하며 # 대체
# insert 함수 사용하자 -> 요소 개수 증가 조심하기!

for i in range(5):
    plus_list = ['+','+','+','+']
    plus_list.insert(i, '#')
    print(''.join(plus_list))
