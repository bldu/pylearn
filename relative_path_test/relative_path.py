import os
import sys


path = os.path.abspath("./")
print("os.path.abspath",path)
# 如果是执行 python relative_path_test/relative_path.py, 则输出为 /xxx/pylearn
# 如果是执行 python relative_path.py, 则输出为 /xxx/pylearn/relative_path_test
# 使用相对路径时，要注意是在哪个路径下执行的 python 命令， 执行 python 命令时所在的路径就是当前工作路径，被执行文件里所写的相对路径就是相对当前工作路径而言的。



print("sys.path", sys.path)
# 执行 python relative_path_test/relative_path.py, 仍然是路径 /xxx/pylearn/relative_path_test 被加入了包搜索路径。即无论工作路径在哪儿，搜索路径永远是被执行文件所在的目录路径。
# 如果是执行 python -m relative_path_test.relative_path, 则是路径 /xxx/pylearn被加入了包搜索路径。
