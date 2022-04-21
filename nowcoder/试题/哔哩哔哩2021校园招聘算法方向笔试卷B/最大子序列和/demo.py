# number = list(map(int, input().split()))  # 把输入直接转成数字
import cProfile
import sys

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
def solver(nums):
    if len(nums) == 0:
        return 0
    end = 0
    sum = 0
    ans = -sys.maxsize
    while end < len(nums):
        sum += nums[end]
        ans = max(ans, sum)
        print(ans)
        if sum < 0:
            sum = 0
        end += 1
    return ans


def main(get_input=input):
    nums = list(map(int, get_input().split(',')))

    print(solver(nums))
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
