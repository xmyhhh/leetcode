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
def solver(s, t):
    s=list(s)
    t=list(t)
    need={}
    for i in t:
        need[i]=need.get(i,0)+1
    have={}
    start=0
    end=0
    s_len=len(s)
    ans_len=s_len
    ans=[]
    def isSuperDict(superDict,subDict):
        subDict_set=set(subDict)
        for i in subDict_set:
            if superDict.get(i,0)<subDict[i]:
                return False
        return True
    while end<s_len:
        have[s[end]]=have.get(s[end],0)+1


        while (isSuperDict(have,need)):

            if (end-start)<ans_len:  #update ans
                ans_len=(end-start)
                ans=[]
                for i in range(start,end+1):
                    ans.append(s[i])

            have[s[start]]-=1
            start+=1
        end+=1
    ans_string=''
    for i in ans:
        ans_string+=i
    return ans_string


def main():
    # N,M=map(int,get_input().split())
    # N = int(get_input())
    s = "ADOBECOSDAGSDAFNC"
    t = "ABCAS"
    print(solver(s, t))
    pass


if __name__ == '__main__':
    cProfile.run("main()")  # test without performance monitor
