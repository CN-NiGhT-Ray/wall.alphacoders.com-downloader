#import csv
import json
import os
import requests
from lxml import etree

class abyss:
    def first(self):
        print('input keyword:', end='')
        self.keyword = 'miku'#self.keyword = str(input())
        self.page_now = 0
        self.page_p_now = 0
        connect(''.join(['https://wall.alphacoders.com/search.php?search=', self.keyword]))
        #print('ok!\nanalysing index...', end = '')
        html = etree.HTML(response.content)
        self.p_num = int(html.xpath('//h1/text()')[0].strip('\n').strip(' ').split(' ')[0])
        self.page_p_num = len(etree.HTML(response.content).xpath('//*[@class="thumb-container-big "]/div[1]/div[1]/a/@href'))
        if self.p_num / self.page_p_num == 1:
            self.lastpage_p_num = self.page_p_num
        else:
            self.lastpage_p_num = self.p_num % self.page_p_num
        self.page_num = self.p_num // self.page_p_num + 1
        '''self.ls_csv = [['keyword', self.keyword], ['p_num', str(self.p_num)], ['page_p_num', str(self.page_p_num)], ['lastpage_p_num', str(self.lastpage_p_num)], ['page_num', str(self.page_num)], ['page_now', str(self.page_now)], ['page_p_now', str(self.page_p_now)]]
        self.write_csv()'''
        self.ls_json = {'keyword': self.keyword, 'p_num': str(self.p_num), 'page_p_num': str(self.page_p_num), 'lastpage_p_num': str(self.lastpage_p_num), 'page_num': str(self.page_num), 'page_now': str(self.page_now), 'page_p_now': str(self.page_p_now)}
        self.write_json()
    '''def read_csv(self):
        self.ls_csv = []
        with open('./cache1.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                self.ls_csv.append(row)
        self.keyword = self.ls_csv[0][-1]# 搜索关键词
        self.p_num = int(self.ls_csv[1][-1])# 搜索结果总数
        self.page_p_num = int(self.ls_csv[2][-1])# 每页显示的结果数（只有一页则为结果总数）
        self.lastpage_p_num = int(self.ls_csv[3][-1])# 最后一页显示的结果数（只有一页则为结果总数）
        self.page_num = int(self.ls_csv[4][-1])# 搜索结果页数
        self.page_now = int(self.ls_csv[5][-1])# 已下载的页数
        self.page_p_now = int(self.ls_csv[6][-1])# 已下载的图片序号'''
    def read_json(self):
        with open('./cache1.json', encoding='utf-8') as file:
            self.ls_json = json.load(file)
        self.keyword = self.ls_json.get('keyword')# 搜索关键词
        self.p_num = int(self.ls_json.get('p_num'))# 搜索结果总数
        self.page_p_num = int(self.ls_json.get('page_p_num'))# 每页显示的结果数（只有一页则为结果总数）
        self.lastpage_p_num = int(self.ls_json.get('lastpage_p_num'))# 最后一页显示的结果数（只有一页则为结果总数）
        self.page_num = int(self.ls_json.get('page_num'))# 搜索结果页数
        self.page_now = int(self.ls_json.get('page_now'))# 已下载的页数
        self.page_p_now = int(self.ls_json.get('page_p_now'))# 已下载的图片序号
    '''def write_csv(self):
        self.ls_csv[5][-1] = str(self.page_now)
        self.ls_csv[6][-1] = str(self.page_p_now)
        with open('./cache1.csv', 'w', newline = '') as file:
            write = csv.writer(file)
            write.writerows(self.ls_csv)'''
    def write_json(self):
        self.ls_json['page_now'] = str(self.page_now)
        self.ls_json['page_p_now'] = str(self.page_p_now)
        with open('./cache1.json', 'w', encoding='utf-8') as file:
            json.dump(self.ls_json, file, indent = 4, ensure_ascii = False)

class abyss_verification:
    def first(self):
        print('input keyword:', end = '')
        self.keyword = 'miku'#self.keyword = str(input())
        self.page_now = 0
        connect(''.join(['https://wall.alphacoders.com/search.php?search=', self.keyword]))
        html=etree.HTML(response.content)
        self.page_num = int(html.xpath('//h1/text()')[0].strip('\n').strip(' ').split(' ')[0]) // len(etree.HTML(response.content).xpath('//*[@class="thumb-container-big "]/div[1]/div[1]/a/@href')) + 1
        '''self.ls_csv = [['keyword', self.keyword], ['page_num', str(self.page_num)], ['page_now', str(self.page_now)]]
        self.write_csv()'''
        self.ls_json = {'keyword': self.keyword, 'page_num': str(self.page_num), 'page_now': str(self.page_now)}
        self.write_json()
    '''def passing_csv(self):
        self.ls_csv = []
        with open('./cache1.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.ls_csv.append(row)
        self.keyword = self.ls_csv[0][-1]# 搜索关键词
        self.page_num = int(self.ls_csv[4][-1])# 搜索结果页数
        self.page_now = 0
        self.ls_csv.clear()
        self.ls_csv = [['keyword', self.keyword], ['page_num', str(self.page_num)], ['page_now', str(self.page_now)]]
        self.write_csv()'''
    def passing_json(self):
        with open('./cache1.json', encoding='utf-8') as file:
            self.ls_json = json.load(file)
        self.keyword = self.ls_json.get('keyword')# 搜索关键词
        self.page_num = int(self.ls_json.get('page_num'))# 搜索结果页数
        self.page_now = int(self.ls_json.get('page_now'))# 已校验的图片页数
        self.ls_json.clear()
        self.ls_json = {'keyword': self.keyword, 'page_num': str(self.page_num), 'page_now': str(self.page_now)}
        self.write_json()
    '''def read(self):
        self.ls_csv = []
        with open('./cache2.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.ls_csv.append(row)
        self.keyword = self.ls_csv[0][-1]# 搜索关键词
        self.page_num = int(self.ls_csv[1][-1])# 搜索结果页数
        self.page_now = int(self.ls_csv[2][-1])# 已校验的图片页数'''
    def read_json(self):
        with open('./cache2.json', encoding='utf-8') as file:
            self.ls_json = json.load(file)
        self.keyword = self.ls_json.get('keyword')# 搜索关键词
        self.page_num = int(self.ls_json.get('page_num'))# 搜索结果页数
        self.page_now = int(self.ls_json.get('page_now'))# 已校验的图片页数
    '''def write_csv(self):
        self.ls_csv[2][-1] = str(self.page_now)
        with open('./cache2.csv', 'w', newline = '') as file:
            write = csv.writer(file)
            write.writerows(self.ls_csv)'''
    def write_json(self):
        self.ls_json['page_now'] = str(self.page_now)
        with open('./cache2.json', 'w', encoding='utf-8') as file:
            json.dump(self.ls_json, file, indent = 4, ensure_ascii = False)

class nhentai:
    def first(self):
        print('input url:', end = '')
        self.url = 'https://nhentai.net/g/234186/'#self.url = str(input())
        connect(self.url)
        html = etree.HTML(response.content)
        self.p_name = html.xpath('//h2/text())')
        self.p_num = len(html.xpath('//*[@class=thumb-container])'))
        self.p_now = 0
        self.ls_json = {'url': self.url, 'p_name': self.p_name, 'p_num': str(self.p_num), 'p_now': str(self.p_now)}
        self.write_json()
    def read_json(self):
        with open('./cache3.json', encoding='utf-8') as file:
            self.ls_json = json.load(file)
        self.url = self.ls_json.get('url')# 链接
        self.p_name = self.ls_json.get('p_name')# 搜索结果标题
        self.p_num = int(self.ls_json.get('p_num'))# 搜索结果页数
        self.p_now = int(self.ls_json.get('p_now'))# 已校验的图片页数
    def write_json(self):
        self.ls_json['p_now'] = str(self.p_now)
        with open('./cache3.json', 'w', encoding='utf-8') as file:
            json.dump(self.ls_json, file, indent = 4, ensure_ascii = False)

def one():
    data1 = abyss()
    #if os.path.isfile('cache1.csv'):# 检测有cache
    if os.path.isfile('cache1.json'):# 检测有cache
        print('Cache found!', end = '')
        data1.read_json()
    else:# 检测无cache
        data1.first()
    if not os.path.isdir(data1.keyword):
        os.mkdir(data1.keyword)
    i = data1.page_now + 1
    j = data1.page_p_now
    count = (i - 1) * data1.page_p_num + j + 1
    while(i < data1.page_num):
        print('geting page:{} index...'.format(i))
        connect(''.join(['https://wall.alphacoders.com/search.php?search=', data1.keyword, '&page=', str(i)]))
        ls_url = etree.HTML(response.content).xpath('//*[@class="thumb-container-big "]/div[1]/div[1]/a/img/@data-src')
        print('ok!')
        while(j < data1.page_p_num):
            print('Downloading page:{}/picture:{}...count:{}...'.format(i, j + 1, count), end = '')
            ls_temp = ls_url[j].split('thumb')
            name = ls_temp.pop(-1).split('-')[-1]
            url = ''.join([ls_temp[0], name])
            path = ''.join(['./', data1.keyword, '/', name])
            connect(url)
            while True:
                with open(path, 'wb') as file:
                    file.write(response.content)
                if os.path.getsize(path) == int(response.headers['content-length']):
                    break
            data1.page_now = i - 1
            j += 1
            data1.page_p_now = j
            data1.write_json()
            count += 1
            print('ok!')
        j = 0
        i += 1
        data1.page_now = i - 1
        data1.page_p_now = j
        data1.write_json()
    print('geting page:{} index...'.format(i))
    connect(''.join(['https://wall.alphacoders.com/search.php?search=', data1.keyword, '&page=', str(data1.page_num)]))
    ls_url = etree.HTML(response.content).xpath('//*[@class="thumb-container-big "]/div[1]/div[1]/a/img/@data-src')
    print('ok!')
    while(j < data1.lastpage_p_num):
        print('Downloading page:{}/picture:{}...count:{}...'.format(data1.page_num, j + 1, count), end = '')
        ls_temp = ls_url[j].split('thumb')
        name = ls_temp.pop(-1).split('-')[-1]
        url = ''.join([ls_temp[0], name])
        path = ''.join(['./', data1.keyword, '/', name])
        connect(url)
        while True:
            with open(path, 'wb') as file:
                file.write(response.content)
            if os.path.getsize(path) == int(response.headers['content-length']):
                break
        data1.page_now = data1.page_num - 1
        j += 1
        data1.page_p_now = j
        data1.write_json()
        count += 1
        print('ok!')
    print('Success!')

def two():
    data2 = abyss_verification()
    #if os.path.isfile('cache2.csv'):# 检测有cache
    if os.path.isfile('cache2.json'):# 检测有cache
        print('Cache found!', end = '')
        data2.read_json()
    else:# 检测无cache
        #if os.path.isfile('cache1.csv'):
        if os.path.isfile('cache1.json'):
            data2.passing_json()
        else:
            data2.first()
    if not os.path.isdir(data2.keyword):
        exit('Folder not found!')
    ls_name = os.listdir(''.join(['./', data2.keyword, '/']))
    data2.p_num = len(ls_name)
    for i in range(data2.p_num):
        ls_name[i] = int(ls_name[i].split('.')[0])
    ls_name = set(ls_name)
    ls_miss = []
    i = data2.page_now
    while(i < data2.page_num):
        print('geting page:{} index...'.format(i + 1))
        connect(''.join(['https://wall.alphacoders.com/search.php?search=', data2.keyword, '&page=', str(i + 1)]))
        ls_url = etree.HTML(response.content).xpath('//*[@class="thumb-container-big "]/div[1]/div[1]/a/@href')
        for url in ls_url:
            url = int(url.split('=')[-1])
            if int(url) not in ls_name:
                ls_miss.append(url)
            else:
                ls_name.remove(url)
        i += 1
        data2.page_now = i
        data2.write_json()
    print('Not found:{}'.format(ls_miss))
    print('Duplicate:{}'.format(ls_name))

def three():
    data3 = nhentai()
    if os.path.isfile('cache3.json'):# 检测有cache
        print('Cache found!', end = '')
        data3.read_json()
    else:# 检测无cache
        data3.first()
    if not os.path.isdir(data3.p_name):
        os.mkdir(data3.p_name)
    i = data3.p_now + 1
    while(i <= data3.p_num):
        print('Downloading {} picture...'.format(i))
        path = ''.join(['./', data3.p_name, '/', str(i)])
        connect(''.join(['https://i.nhentai.net/galleries/1227652/', str(i), '.jpg']))
        while True:
            with open(path, 'wb') as file:
                file.write(response.content)
            if os.path.getsize(path) == int(response.headers['content-length']):
                break
        data3.p_now = i
        i += 1
        data3.write_json

def connect(url):# 不需要全局，不返回，返回response全局
    num = 0
    while(num <= 6):
        try:
            global response
            response = requests.get(url, timeout = 5)
        except:
            num += 1
            print('Try to connect...(count {} )'.format(num))
        else:
            break
    else:
        exit('connect error!')

print('Connect to wall.alphacoders.com...')
#connect('https://wall.alphacoders.com/')
#print('{}ms\n{:=^25}\n1.get pictures\n2.verify pictures\n{:=^25}\nInput option:'.format(response.elapsed.microseconds // 1000, '=', '='), end = '')
options_main = {1:one, 2:two, 3:three}
flag = 3#flag = input()
options_main.get(flag)()
print('success!')
