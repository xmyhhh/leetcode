# number = list(map(int, input().split()))  # 把输入直接转成数字
import cProfile

MOD = 1000000007


# 定义input辅助函数（从文件加载模拟输入）
class InputHelper:
    def __init__(self, path="./input_data.txt"):
        with open(path) as file:
            self.lines = file.readlines()
        self.currentLine = -1

    def getInput(self):
        self.currentLine += 1
        return self.lines[self.currentLine]


# 定义测试样例class
class sample:
    def __init__(self, A, B, n):
        self.A = A
        self.B = B
        self.n = n


# 定义处理函数
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


def main(get_input=input):
    sample_list = []
    N = int(get_input())

    # 处理输入生成测试样例list
    for i in range(N):
        number = list(map(int, get_input().split()))
        sample_list.append(sample(number[0], number[1], number[2]))

    # 逐个处理测试样例
    for item in sample_list:
        print(solver(item.A, item.B, item.n))

    # 逐个处理测试样例
    for item in sample_list:
        print(solver(item.A, item.B, item.n))


if __name__ == '__main__':
    using_input_helper = True
    if using_input_helper:
        inputHelper = InputHelper()
        cProfile.run("main(inputHelper.getInput)")  # test with performance monitor
        # main(inputHelper.getInput)  #test without performance monitor
    else:
        # cProfile.run("main()")  #test with performance monitor
        main()  # test without performance monitor
