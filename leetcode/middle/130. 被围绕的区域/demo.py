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
def solver(board):
    if not board:
        return

    n, m = len(board), len(board[0])

    def dfs(x, y):
        if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
            return

        board[x][y] = "A"
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    for i in range(n):
        dfs(i, 0)
        dfs(i, m - 1)

    for i in range(m - 1):
        dfs(0, i)
        dfs(n - 1, i)

    for i in range(n):
        for j in range(m):
            if board[i][j] == "A":
                board[i][j] = "O"
            elif board[i][j] == "O":
                board[i][j] = "X"


def main(get_input=input):
    board = []
    m, n = map(int, get_input().split())
    for i in range(m):
        board.append(list(get_input().split()))

    print(solver(board))
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
