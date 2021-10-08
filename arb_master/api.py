import asyncio

from utils import digest_binance_response

BINANCE = 'https://api1.binance.com/api/v3/'


async def get_depth(session, url):
    resp = await session.get(url)
    return await resp.json()


async def get_all_depth(session, urls):
    tasks = [get_depth(session, url) for url in urls]
    return await asyncio.gather(*tasks)


async def get_depth_binance(session, pair, limit=5):
    url = BINANCE+f'depth?symbol={pair}&limit={limit}'
    response = await get_depth(session, url)
    return digest_binance_response(response)


async def get_all_depth_binance(session, pairs, limit=5):
    urls = [BINANCE+f'depth?symbol={pair}&limit={limit}' for pair in pairs]
    responses = await get_all_depth(session, urls)
    return [digest_binance_response(r) for r in responses]
