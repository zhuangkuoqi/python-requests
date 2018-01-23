import requests

def translate(url,kw):
    res = requests.post(url,data = {'kw':kw})
    data = res.json()['data']
    print('翻译结果为：')
    for d in data:
        print(d['k'],':',d['v'])

if __name__ == '__main__':
    url = 'http://fanyi.baidu.com/sug'
    kw = input('输入要翻译的单词或句子(按"q"结束):')
    translate(url,kw = kw)
