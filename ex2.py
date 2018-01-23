import requests
import re
import os


def changeImgSrc(src):
    imgname = src[7:13]   #后期修改
    result_src = 'http://#######'+src
    result_src = result_src.replace('small','big')
    return result_src,imgname


def getImgUrlList(url,params):
    res = requests.get(url,params=params)
    list_img_src = re.findall('images.*?\.bmp',res.text)
    result_list_img_src = {}
    for src in list_img_src:
        result_src,imgname  = changeImgSrc(src)
        result_list_img_src[imgname] = result_src
    return result_list_img_src

#这是修改后的内容，………………………………………………
def downloadImg(result_list_img_src,dir):

    for imgkey in result_list_img_src:
        res = requests.get(result_list_img_src[imgkey])
        file = open(dir+imgkey+'.bmp','wb')
        file.write(res.content) 
        file.close()
        print('download '+imgkey+'.bmp')

    print('download finish.')

def main():
    start_url = 'http://#######'
    for page in range(1,1001):
        os.mkdir('img/'+str(page))
        result_list_img_src = getImgUrlList(start_url,{'idx':str(page)})
        downloadImg(result_list_img_src,'img/'+str(page)+'/')

if __name__ == '__main__':
    res = requests.get('http://dp.gaga.me/depositphotos/1024/2017/1031/cd6dbca788c49b0760c887f267ddd9bd.jpg?watermark/1/image/aHR0cDovL3Jlcy5nYWdhLm1lL3dhdGVybWFyay9wYWl4aW4xLnBuZz9pbWFnZVZpZXcyLzIvdy8zMDAvaC8zMDA=/dissolve/35/gravity/Center/ws/1&amp;e=1516613938&amp;token=oVzGH3GXS72ah4todWOUas5zZ2ZoLSXxJa2civF0:_w5Mvt4omc7OIpq2Ci592JsB5bc=')
    file = open('b.jpg','wb')
    file.write(res.content)
    file.close()
