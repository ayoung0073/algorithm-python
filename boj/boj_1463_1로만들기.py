x = int(input())                                                  

# 계산된 결과를 저장하기 위한 배열 초기화 (0 ~ x이므로 x+1개의 크기 필요)
d = [0] * (x + 1)

# 다이나믹 프로그래밍 (bottom-up)
# i가 x가 될 때까지 연산의 수
for i in range(2, x + 1): # 1이 되기위한 연산 수는 0이므로 2부터 시작
  # (i-1) -> i가 될때 1을 더하므로 연산 수 + 1
  d[i] = d[i - 1] + 1
  
  # i가 2로 나누어 떨어질 경우
  # if 3으로 나누어떨어지는 경우가 연산 수를 더 적게 하는 것이므로, % 2 먼저 비교 후, % 3 비교
  if i % 2 == 0:
  	# (i-1)의 값에서 + 1 연산수 vs 2를 곱하고 + 1 연산수 중 작은 걸 택한다
    d[i] = min(d[i], d[i // 2] + 1) # 연산 수 비교
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)

print(d[x])
