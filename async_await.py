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

def main():
    foo() # 只会得到一个 coroutine 对象，不会执行
    asyncio.run(foo())
    asyncio.run(bar())
  


if __name__ == "__main__":
    main()