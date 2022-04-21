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
def solver(X,Y):
    #n^2时间复杂度
    N=len(X)
    nums_dict={}
    ans=1
    for i in range (N): #假设直线过点i
        k_dict={}
        ans_i=1 #经过点i的直线，最多可经过的点，初始为1
        for j in range(N):  #分别计算节点i和其他节点j之间的斜率
            if i==j:
                continue
            if X[i]==X[j]:
                k="stright"
            else:
                k=(Y[i]-Y[j])/(X[i]-X[j])
            k_dict[k]=k_dict.get(k,1)+1
            ans_i=max(ans_i,k_dict[k])
        ans=max(ans,ans_i)
    return ans



def main(get_input=input):
    N = int(get_input())
    X,Y=[],[]
    for i in range(N):

        x,y=map(int,get_input().split())
        X.append(x)
        Y.append(y)

    print(solver(X,Y))
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
