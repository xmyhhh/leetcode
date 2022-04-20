# number = list(map(int, input().split()))  # 把输入直接转成数字


import cProfile
import copy

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
def solver(N, nums):
    nums_before = copy.copy((nums))
    nums_after = []
    last_nums_after_len = 0
    play_times = 0
    if len(nums_before) == 0:
        return 0
    while (1):
        i = 0
        j = 1
        nums_after.append(nums_before[0])
        while i < (len(nums_before) - 1):

            if j < len(nums_before) and nums_before[i] > nums_before[j]:  # 如果左边大于右边，递减，跳过
                j += 1
                i += 1
            else:  # 如果右边大于左边，递增，保留
                j += 1
                i += 1
                nums_after.append(nums_before[i])
        if last_nums_after_len == len(nums_after):
            break
        else:
            play_times += 1
            last_nums_after_len = len(nums_after)
        nums_before = nums_after
        nums_after = []
        if nums_before==nums:
            return 0
    return play_times


def main(get_input=input):
    # N,M=map(int,get_input().split())
    N = int(get_input())
    nums = list(map(int, get_input().split()))
    print(solver(N, nums))
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
