"""
This is a simple example about python requests library
"""

import requests

def translate(url,kw):
    """
    This function just for the fanyi.baidu.com and the url is http://fanyi.baidu.com/sug .
    Give a word or a sentence that you want to translate and return the result.

    :param url: must be the url http://fanyi.baidu.com/sug
    :param kw: a word or a sentence.
    :return: the reuslt about the translate.
    """
    res = requests.post(url,data = {'kw':kw})
    data = res.json()['data']
    print('result:',end='\n')
    for d in data:
        print(d['k'],':',d['v'])    