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
def solver(height):
    ans = 0
    height_len = len(height)
    left_max_dp=[0]*height_len
    right_max_dp=[0]*height_len

    for i in range(height_len-2,-1,-1):  #更新 right_max_dp
        right_max_dp[i]=max(right_max_dp[i+1],height[i+1])
    for i in range(1,height_len):
        left_max_dp[i]=max(left_max_dp[i-1],height[i-1])
    for i in range(height_len):
        ans+= max(min(left_max_dp[i],right_max_dp[i])-height[i],0)
        print(min(left_max_dp[i],right_max_dp[i]))
    return ans



def main(get_input=input):

    N=list(map(int,get_input().split(',')))
    # N = int(get_input())

    print(solver(N))
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
