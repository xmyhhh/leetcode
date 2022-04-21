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
def solver(string):
    string_list = list(string)
    string_len = len(string_list)

    dp = [[False] * string_len for _ in range(string_len)]
    max_len=0
    ans=[]
    for j in range(string_len):  # 注意必须一列列填
        for i in range(0,j+1):

            if j-i==1 and string_list[i]==string_list[j]:  #两个字符
                dp[i][j]=True
                if max_len<2:
                    max_len=2
                    ans=string_list[i:j+1]
            elif i==j:  #一个字符
                dp[i][j]=True
                if max_len<1:
                    max_len=1
                    ans=string_list[i:j+1]
            elif (string_list[i]==string_list[j] and dp[i+1][j-1]):       #三个以上字符
                dp[i][j]=True
                if max_len<(j-i+1):
                    max_len=j-i+1
                    ans=string_list[i:j+1]
    ans_string=""
    for i in ans:
        ans_string+=i
    return ans_string
    pass


def main(get_input=input):
    string = get_input()
    # N = int(get_input())

    print(solver(string))
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
