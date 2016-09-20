#异步爬取
import os
import time
import asyncio
from aiohttp import ClientSession


async def down(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            name = 'picture' + '/' + url.split('=')[-1]
            with open(name,'wb') as code:
                code.write(response)

if __name__ == '__main__':
    if not os.path.exists('picture'):
        os.mkdir('picture')
    start = time.clock()
    loop = asyncio.get_event_loop()
    tasks = []
    url = 'http://www.jikexueyuan.com/course/?pageNum={}'
    for i in range(1,5):
        print(url.format)
        task = asyncio.ensure_future(down(url.format(i)))
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.clock()
    print('read: %f s' % (end - start))

