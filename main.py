import problem.easy.m9


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    Solution_level = "easy"

    # Solution_level = "middle"

    # Solution_level = "hard"
    Solution_num = 234
    import_string = "from problem." + Solution_level + " import m" + str(Solution_num) + " as m"
    exec(import_string)
    solution = m.Solution() #编译器报错正常
    solution.run()
    pass
