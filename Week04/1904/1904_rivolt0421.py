n = int(input())

# lesson 피보나치 이렇게도 쓸 수 있구나. 메모리가 많이 줄어듦.
d = [2, 1]
   #[짝,홀]
   #[0, 1]  <- index
   
for i in range(3, n+1):
    d[i%2] = (d[0] + d[1]) % 15746
    
print(d[n])

# 먼저 길이가 i인 수를 만든다고 생각해보자. 그러면 사용할 수 있는 숫자 카드는 00과 1이다.
# 즉, 이전에 만든 수에다가 00을 붙이거나, 1을 붙여서 만든다는 얘기가 된다.
# 그런데 잘 생각해보면 00은 길이가 2이기 때문에 i-1번째에서는 붙일 수가 없다.
# 따라서 i-2번째에서 00을 붙여 만드는 경우와 i-1번째에서 1을 붙여 만들 수 있는 경우의 합이다.

# 왜 i-2번째에서 1을 2개 붙여 만드는 경우는 생각하지 않는가?
# 그 이유는 바로 i-1번째에서 1을 붙여 만드는 경우와 중복되기 때문에다. 

# 따라서 N-2에선 00만 붙이고, N-1에선 1만 붙여 만든다고 정해보자.
# 그리고 수를 붙여줄 때 N-2의 경우의 수들엔 "맨 뒤에" 00을 붙이고, N-1의 경우의 수들엔 "맨 앞에" 1을 붙이는 규칙으로 만들어 보자.

# N = 5 를 구하려고 할 때.
#
# N=3인 경우 -> 001,100,111
# ⬇
# N-2의 맨 뒤에 00추가 -> 00100,10000,11100
#
# N=4인 경우 -> 0011, 0000, 1001, 1100, 1111
# ⬇
# N-1의 맨 앞에 1 추가-> 10011,10000,11001,1100,11111

# 이렇게 총 8개로 자연스럽게 중복이 제거되면서 값이 나오는 걸 볼 수 있다.