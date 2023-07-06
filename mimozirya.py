import asyncio
k = 0.1
async def loundary():
    print('начали стирку')
    await asyncio.sleep(70*k)
    print('закончили стирку')

async def soup():
    print('начали готовить')
    await asyncio.sleep(60*k)
    print('едим суп')

async def tea():
    print('чайник на плите')
    await asyncio.sleep(15*k)
    print('щай щай')

async def sync_main():
    await loundary()
    await soup()
    await tea()

async def async_main():
    await asyncio.gather(loundary(),soup(),tea())
asyncio.run(async_main())