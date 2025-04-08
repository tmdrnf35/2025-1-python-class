# 2025.4.2 파이썬수업 프로젝트 두번째
# 콜라츠 추측, 또는 우박수
# 1부터 100까지숫자중, 가장많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장많은 단계는 몇단계인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3 * n + 1
#  예: 5 -> 16 -> 8 -> 4 -> 2 -> 1 (5단계)
n = 97
# 단계의 갯수를 셀것 - done
# n을 1부터 99까지 변화하면서, 각각의 단계수를 출력할 것
# 그중 가장 큰 수를 찾을 것
# n=97: 118번만에 1로 도달
# n=73: 115번만에 1로 도달

maxvalue = 0
maxvaluen = 0
secondvalue = 0
secondvaluen = 0
thirdvalue = 0
thirdvaluen = 0

for n in range(1, 100):
    i = n
    ncount = 0

    while i != 1:
        if i % 2 == 1:
            i = 3 * i + 1
        else:
            i = i // 2
        ncount = ncount + 1

    print(f'{ncount}')

    if maxvalue < ncount:

        thirdvalue = secondvalue
        thirdvaluen = secondvaluen

        secondvalue = maxvalue
        secondvaluen = maxvaluen


        maxvalue = ncount
        maxvaluen = n

    elif secondvalue < ncount:

        secondvalue = ncount
        secondvaluen = n

    elif thirdvalue < ncount:
        thirdvalue = ncount
        thirdvaluen = n

print(f'{maxvalue=}, {maxvaluen=}')
print(f'{secondvalue=}, {secondvaluen=}')
print(f'{thirdvalue=}, {thirdvaluen=}')



