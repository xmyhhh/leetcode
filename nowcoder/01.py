# number = list(map(int, input().split()))  # 把输入直接转成数字

MOD = 1000000007


# 定义测试样例class
class sample:
    def __init__(self, A, B, n):
        self.A = A
        self.B = B
        self.n = n


# 定义处理函数
# def solver(A, B, n):
#
#
#     num_0 = 2
#     num_1 = A
#     if n == 1:
#         return num_1
#     if n == 0:
#         return num_0
#     for i in range(2, n):
#         a = num_1
#         num_1 = A * num_1 - B * num_0
#         num_0 = a
#
#     return (A * num_1 - B * num_0) % MOD

def solver(a, b, n):
    def matrix_mul(ma, mb):
        ans = [[0] * 2 for _ in range(2)]
        for i in range(2):
            for j in range(2):
                ans[i][j] = ma[i][0] * mb[0][j] + ma[i][1] * mb[1][j]
                if ans[i][j] >= 0:
                    ans[i][j] %= MOD
                else:
                    ans[i][j] = - (abs(ans[i][j]) % MOD)
        return ans

    def matrix_pow(matrix, n):
        ans = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1 != 0:
                ans = matrix_mul(ans, matrix)
            n >>= 1
            matrix = matrix_mul(matrix, matrix)
        return ans

    if n == 1:
        return a
    matrix = [[a, -b], [1, 0]]
    res = matrix_pow(matrix, n - 1)
    return (res[0][0] * a + res[0][1] * 2) % MOD


sample_list = []
N = int(input())

# 处理输入生成测试样例list
for i in range(N):
    number = list(map(int, input().split()))
    sample_list.append(sample(number[0], number[1], number[2]))

# 逐个处理测试样例
for item in sample_list:
    print(solver(item.A, item.B, item.n))
