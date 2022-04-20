# number = list(map(int, input().split()))  # 把输入直接转成数字
import cProfile


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
    def __init__(self, goodsNums, goods_list1, goods_list2):
        self.goodsNums = goodsNums
        self.goods_list1 = goods_list1
        self.goods_list2 = goods_list2


# 定义处理函数
def solver(goodsNums, goods_list1, goods_list2):
    list1, list2 = zip(*(sorted(zip(goods_list1, goods_list2), key=lambda x: (x[0], -x[1]))))

    def Longest_Incremental_Subsequence(nums):
        if not nums:
            return 0
        # 最小递增子序列
        num_len = len(nums)

        dp = [1] * num_len
        for i in range(num_len):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    return Longest_Incremental_Subsequence(list2)


def main(get_input=input):
    sample_list = []

    N = int(get_input())

    # 处理输入生成测试样例list
    for i in range(N):
        goodsNums = int(get_input())
        goods_list1 = list(map(int, get_input().split()))
        goods_list2 = list(map(int, get_input().split()))
        sample_list.append(sample(goodsNums, goods_list1, goods_list2))

    # 逐个处理测试样例
    for item in sample_list:
        print(solver(item.goodsNums, item.goods_list1, item.goods_list2))


if __name__ == '__main__':
    using_input_helper=True
    if using_input_helper:
        inputHelper=InputHelper()
        cProfile.run("main(inputHelper.getInput)")  #test with performance monitor
        # main(inputHelper.getInput)  #test without performance monitor
    else:
        # cProfile.run("main()")  #test with performance monitor
        main()  # test without performance monitor