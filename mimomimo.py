import asyncio
import random


async def kachkach(i):
    print('котенок ', i, ' начал скачиваниe')
    await asyncio.sleep(random.random())
    print('котенок ', i, ' закончил скачиваниe')


async def main(n: int = 10):
    """n - количество котят"""
    a = []
    for i in range(n):
        a.append(kachkach(i))
    await asyncio.gather(*a)



asyncio.run(main(10))

