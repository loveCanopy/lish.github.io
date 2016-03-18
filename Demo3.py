__author__ = 'Sherlock'
import urllib.request as u
import os

def url_open(url):
    req = u.Request(url)
    req.add_header('User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
    response = u.urlopen(url)
    html = response.read()
    return html

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img id="maxImg1" src=')
    b = html.find('.jpg', a , a+255)
    if b !=-1:
        img_addrs.append(html[a+22:b+4])

    #print(img_addrs[0])
    return img_addrs[0]


def save_imgs(folder, img_address):
    filename = img_address.split('/')[-1]
    with open(filename, 'wb') as f:
        img = url_open(img_address)
        f.write(img)

def download_mm(folder = 'jiandan', pages = 100):
    # 生成文件夹
    os.mkdir(folder)
    # 改变工作目录
    os.chdir(folder)

    url = 'http://www.chunmm.com/meixiong/50213-'
    #page_num = int(get_page(url))

    for i in range(1,pages):
        #page_num -= i
        page_url = url + str(i) + '.html'

        img_address = find_imgs(page_url)
        save_imgs(folder, img_address)

if __name__ == '__main__':
    download_mm()