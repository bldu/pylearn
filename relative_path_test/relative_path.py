import os


path = os.path.abspath("./")
print(path)
# 如果是执行 python relative_path_test/relative_path.py, 则输出为 /xxx/pylearn
# 如果是执行 python relative_path.py, 则输出为 /xxx/pylearn/relative_path_test
# 使用相对路径时，要注意是在哪个路径下执行的 python 命令， 执行 python 命令时所在的路径就是当前工作路径，被执行文件里所写的相对路径就是相对当前工作路径而言的。
