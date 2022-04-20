# number = list(map(int, input().split()))  # 把输入直接转成数字
import cProfile

MOD = 1e+3


# 定义input辅助函数（从文件加载模拟输入）
class InputHelper:
    def __init__(self, path="./input_data.txt"):
        with open(path) as file:
            self.lines = file.readlines()
        self.currentLine = -1

    def getInput(self):
        self.currentLine += 1
        return self.lines[self.currentLine]


# 定义处理函数
def solver(N, envelopes_w, envelopes_h):
    # 先对宽度 w 进行升序排序，如果遇到 w 相同的情况，则按照高度 h 降序排序；之后把所有的 h 作为一个数组，在这个数组上计算 LIS 的长度就是答案
    # 注意高度 h 是降序排序，确保在w相同的时候，只有一个h可以被选中
    envelopes_w_sort, envelopes_h_sort = zip(*sorted(zip(envelopes_w, envelopes_h), key=lambda x: (x[0], x[1])))

    def LIS(nums):
        if not nums:
            return 0
        N = len(nums)
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    return LIS(envelopes_h_sort)


def main(get_input=input):
    N = int(get_input())
    envelopes_w = []
    envelopes_h = []
    for i in range(N):
        w, h = map(int, get_input().split())
        envelopes_w.append(w)

        envelopes_h.append(h)
    print(solver(N, envelopes_w, envelopes_h))

    pass


if __name__ == '__main__':
    using_input_helper = True
    if using_input_helper:
        inputHelper = InputHelper()
        cProfile.run("main(inputHelper.getInput)")  # test with performance monitor
        # main(inputHelper.getInput)  #test without performance monitor
    else:
        # cProfile.run("main()")  #test with performance monitor
        main()  # test without performance monitor
