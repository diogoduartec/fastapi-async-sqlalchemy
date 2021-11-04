from datetime import datetime

from aiohttp import ClientSession
from asyncio import gather, run

from database.init_db import create_database
from services import UserService, FavoriteService


async def populate():
    symbols = ['BTC', 'ETH', 'MATIC', 'AAVE', 'AAVE', 'LINK', 'LTC', 'MANA', 'SUSHI', 'XRP']
    await create_database()
    await gather(*[UserService.create_user(name=f'name{i}') for i in range(10)])
    tasks = []
    
    for i in range(10):
        tasks += [FavoriteService.add_favorite(user_id=i+1, symbol=symbols[j%10]) for j in range(10)]
    
    await gather(*tasks)


run(populate())