"""
await 只能在 async def 里用。

asyncio.run() 只能调用一次（不能在已有事件循环里嵌套）。

协程必须用 await 或 asyncio.run() 执行，否则不会真的运行。
"""

import asyncio

async def foo():
    print("foo()")


async def bar():
    print("bar() begin")
    await foo()
    print("bar() end")


def test1():
    foo() # 只会得到一个 coroutine 对象，不会执行
    asyncio.run(foo())
    asyncio.run(bar())


async def task(name, delay):
    print(f"Task {name} start")
    await asyncio.sleep(delay)
    print(f"Task {name} end")
    return name

async def concurrent1():
    print("concurrent1")
    # 方式1：gather并发执行
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
    )
    print("Results:", results)


async def concurrent2():
    print("concurrent2")
    # 方式2：create_task 手动调度
    t1 = asyncio.create_task(task("C", 1))
    t2 = asyncio.create_task(task("D", 2))
    r1 = await t1
    r2 = await t2
    print(f"Result: {[r1, r2]}")


def test2():
    asyncio.run(concurrent1())
    asyncio.run(concurrent2())


def main():
    # test1()
    test2()


if __name__ == "__main__":
    main()
