import os
import re
import requests
import time
import base64
from bs4 import BeautifulSoup

page = input('页码数从1开始:')
fid = input('版块fid:')
CLSQ = input('输入墙外域名:如(http://cl.ae5.xyz/):')

COUNT = 0


def download(url, name):
    global COUNT
    tm = time.time()
    tm = str(tm)[0:10]
    b64 = base64.b64encode(tm.encode()).decode()
    dir = (\\"{}/{}/{}\\".format(time.strftime(\\"%Y%m%d%H\\"), fid, page))
    if not os.path.exists((dir)):
        os.makedirs((dir))
    try:
        req = queryurl(\\"{}{}\\".format(CLSQ, url))
        find_hash = re.findall(r'hash=(.+?)\&z', req.decode('gbk'))
    except Exception as e:
        print('{}{} 错误为:{}'.format(url, name, e))
        pass
    try:
        get_torrent_url = 'http://www.rmdown.com/download.php?ref={}&reff={}&submit=download'.format(find_hash[0], b64)
        torrent = queryurl(get_torrent_url)
    except Exception as e:
        print('{}{} 错误为:{}'.format(url, name, e))
        pass
    try:
        r = '[’!\\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
        with open(file='{}/{}.torrent'.format(dir, re.sub(r, '', name)), mode='wb') as f:
            f.write(torrent)
        COUNT += 1
        print(\\"共计成功{}次\\".format(COUNT))
        except Exception as e:
        print('{}{} 错误为:{}'.format(url, name, e))
        pass


def queryurl(URL):
    content = requests.get(URL).content
    return content


if __name__ == '__main__':
    ClIndex = '{}thread0806.php?fid={}&search=&page={}'.format(CLSQ, fid, page)
    AllUrl = queryurl(ClIndex)
    soup = BeautifulSoup(AllUrl, 'lxml')
    datas = soup.select('h3 a')
    for item in datas:
        download(item['href'], item.string)
