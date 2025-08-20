import asyncio

async def foo():
    print("hi")

async def bar():
    await foo()

def main():
    asyncio.run(bar())
    asyncio.run(foo())


if __name__ == "__main__":
    main()