#多线程爬取
import re
import os
import time
import random
import requests
from multiprocessing.dummy import Pool as ThreadPool
def down(url):
    httphead = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    r = requests.get(url, headers=httphead)
    name = 'picture1' +'/' + url.split('=')[-1]
    with open(name,'w') as code:
        code.write(r.text)
if __name__ == '__main__':
    start = time.clock()
    pool = ThreadPool(4)
    page = []
    url = 'http://www.jikexueyuan.com/course/?pageNum={}'
    if not os.path.exists('picture1'):
        os.mkdir('picture1')
    for i in range(1,5):
        page.append(url.format(i))
    results = pool.map(down,page)
    pool.close()
    pool.join()
    end = time.clock()
    print('read: %f s' % (end - start))
