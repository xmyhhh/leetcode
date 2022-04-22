# number = list(map(int, input().split()))  # 把输入直接转成数字
#有个物品，每个物品有个属性，第件物品的第个属性用一个正整数表示记为，两个不同的物品被称为是完美对的当且仅当，求完美对的个数。
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


# 定义处理函数
def solver(n, k, goods):
    hash_dict = {}
    ans = 0
    for good in goods:
        def countDetal(good):
            res = []
            for i in range(1, len(good)):
                res.append(good[i] - good[i - 1])
            return tuple(res)

        res = countDetal(good)
        hash_dict[res] = hash_dict.get(res, 0) + 1
        if hash_dict.get(tuple(map(lambda x: -x, res)), None):
            ans += hash_dict[tuple(map(lambda x: -x, res))]

    return ans


def main(get_input=input):
    n, k = map(int, get_input().split())
    goods = []
    for i in range(n):
        goods.append(list(map(int, get_input().split())))

    print(solver(n, k, goods))


if __name__ == '__main__':
    using_input_helper = True
    if using_input_helper:
        inputHelper = InputHelper()
        cProfile.run("main(inputHelper.getInput)")  # test with performance monitor
        # main(inputHelper.getInput)  #test without performance monitor
    else:
        # cProfile.run("main()")  #test with performance monitor
        main()  # test without performance monitor
