import aiohttp
import asyncio

url = 'https://api.thecatapi.com/v1/images/search?limit=10'
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def kachkach(session: aiohttp.ClientSession, url: str, i: int):

    format = url[-3:]

    print('котенок ', i, ' начал скачиваниe')
    response = await session.get(url)
    res_by = await response.read()
    file = open(f'cat{i}.{format}', 'wb')
    file.write(res_by)
    file.close()
    print('котенок ', i, ' закончил скачиваниe')


async def main(n: int = 10):
    """n - количество котят"""
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        response_json = await response.json()

        url_cats = []
        for data in response_json:
            url_cats.append(data['url'])

        a = []
        for i in range(10):
            a.append(kachkach(session, url_cats[i],i))
        await asyncio.gather(*a)

        response.release()

asyncio.run(main(10))