import asyncio

class CoundDown:

    def __init__(self, sec: int, name: str) -> None:
        self.sec = sec
        self.name = name

    async def start(self):
        for i in range(self.sec, 0, -1):
            await asyncio.sleep(1)
            print(f'{self.name}:\t{i}')
        self.ready()

    def ready(self):
        print(f'{self.name} done!')

async def main():
    cd = CoundDown(5, 'lel')
    cd2 = CoundDown(2, 'lal')

if __name__ == '__main__':
    asyncio.run(main())
