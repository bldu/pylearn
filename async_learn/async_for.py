import asyncio

class AsyncCounter:
    def __init__(self, limit):
        self.i = 0
        self.limit = limit

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.i < self.limit:
            await asyncio.sleep(1)  # 模拟异步操作
            self.i += 1
            return self.i
        else:
            raise StopAsyncIteration

async def main():
    async for num in AsyncCounter(5):
        print(num)


if __name__ == "__main__":
    asyncio.run(main())
