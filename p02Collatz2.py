# 2025.4.2 파이썬수업 프로젝트 두번째
# 콜라츠 추측, 또는 우박수
# 1부터 100까지숫자중, 가장많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장많은 단계는 몇단계인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3 * n + 1
#  예: 5 -> 16 -> 8 -> 4 -> 2 -> 1 (5단계)
import numpy as np
import  statistics
import time

from p02Collatzfunc import collatz
MAXNUM = 100

# 2025.4.9. 우박수프로젝트 두번째: 기본 통계량 구하기
# numpy 배열, list 두가지 방식으로 시험
# 구하는 통계량: 최댓값평균, 중앙값, 표준편차, 최빈값,



# 리스트방식

start = time.time()
ncountl = []

for n in range(1, MAXNUM):
    ncount = collatz(n)
    ncountl.append(ncount)

# print(ncountl)
# print(statistics.mean(ncountl))
nmax = 0
unique_sorted = sorted(set(ncountl), reverse=True)
# 최대값, 평균, 중앙값, 표준편차, 최빈값,

print(f'최대값 = {max(ncountl):}')
print(f'1등 숫자 = {ncountl.index(unique_sorted[0]) + 1}')
print(f'2등 숫자 = {ncountl.index(unique_sorted[1]) + 1}')
print(f'3등 숫자 = {ncountl.index(unique_sorted[2]) + 1}')
print(f'평균 = {statistics.mean(ncountl):.5f}')
print(f'중앙값 = {statistics.median(ncountl):}')
# print(f'최빈값 = {statistics.mode(ncountl):.5f}')
print(f'표준편차 = {statistics.stdev(ncountl):.5f}')

end = time.time()
print(f'{end - start:.5f} 초가 걸렸습니다')




# numpy 방식
start = time.time()
ncounta = np.zeros(MAXNUM-1)
for n in range(1, MAXNUM):
    ncount = collatz(n)
    ncounta[n-1] = ncount

top3 = np.argsort(ncounta)[-3:][::-1]

# # 최대값, 평균, 중앙값, 표준편차, 최빈값,

print(f'최대값 = {np.max(ncounta):.5f}')
print(f'1등: 숫자 = {top3[0] + 1}')
print(f'2등: 숫자 = {top3[1] + 1}')
print(f'3등: 숫자 = {top3[2] + 1}')
print(f'평균 = {np.mean(ncounta):.5f}')
print(f'중앙값 = {np.median(ncounta):.5f}')
print(f'표준편차 = {np.std(ncounta):.5f}')
# print(f'최빈값 = {np.bincount(ncounta).argmax():.5f}')
end = time.time()
print(f'{end - start:.5f} 초가 걸렸습니다')