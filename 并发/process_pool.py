"""进程池的使用有四种方式：apply_async、apply、map_async、map。其中apply_async和map_async是异步的，也就是启动进程函数之后会继续执行后续的代码不用等待进程函数返回。apply_async和map_async方式提供了一写获取进程函数状态的函数： ready()、 successful()、 get()。
PS：join()语句要放在close()语句后面。

"""

import multiprocessing
import time


def func(msg):
    print('msg: ', msg)
    time.sleep(1)
    print('********')
    return 'func_return: %s' % msg

def main1():
    # apply_async
    print('\n--------apply_async------------')
    pool = multiprocessing.Pool(processes=4)
    results = []
    for i in range(10):
        msg = 'hello world %d' % i
        result = pool.apply_async(func, (msg, ))
        results.append(result)
    print('apply_async: 不堵塞')

    for i in results:
        i.wait()  # 等待进程函数执行完毕

    for i in results:
        if i.ready():  # 进程函数是否已经启动了
            if i.successful():  # 进程函数是否执行成功
                print(i.get())  # 进程函数返回值


def main2():
    # apply
    print('\n--------apply------------')
    pool = multiprocessing.Pool(processes=4)
    results = []
    for i in range(10):
        msg = 'hello world %d' % i
        result = pool.apply(func, (msg,))
        results.append(result)
    print('apply: 堵塞')  # 执行完func才执行该句
    pool.close()
    pool.join()  # join语句要放在close之后
    print(results)


def main3():
    # map
    print('\n--------map------------')
    args = [1, 2, 4, 5, 7, 8]
    pool = multiprocessing.Pool(processes=5)
    return_data = pool.map(func, args)
    print('堵塞')  # 执行完func才执行该句
    pool.close()
    pool.join()  # join语句要放在close之后
    print(return_data)


def main4():
    # map_async
    print('\n--------map_async------------')
    args = [1, 2, 4, 5, 7, 8]
    pool = multiprocessing.Pool(processes=5)
    result = pool.map_async(func, args)
    print('ready: ', result.ready())
    print('不堵塞')
    result.wait()  # 等待所有进程函数执行完毕

    if result.ready():  # 进程函数是否已经启动了
        if result.successful():  # 进程函数是否执行成功
            print(result.get())  # 进程函数返回值




if __name__ == '__main__':
    #main1()
    #main2()
    main3()
    #main4()
