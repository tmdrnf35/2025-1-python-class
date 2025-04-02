# 2025.4.2 파이썬수업 프로젝트 두번째
# 콜라츠 추측, 또는 우박수
# 1부터 100까지숫자중, 가장많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장많은 단계는 몇단계인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3 * n + 1
#  예: 5 -> 16 -> 8 -> 4 -> 2 -> 1 (5단계)
# n = 97
def collatz_steps(n):
    steps = 0
    while n!= 1:
        if n % 2 == 1:
            n = 3 * n + 1
    else:
        n = n // 2
    steps += 1
    return steps
max_steps = 0
for i in range(1, 101):






