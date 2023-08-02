# import urllib.request
# import urllib.parse
# import re
# import os
#
# path = "/data_image/bg_pic"
# #添加header，其中Referer是必须的,否则会返回403错误，User-Agent是必须的，这样才可以伪装成浏览器进行访问
# header=\
# {
#      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
#      "referer":"https://image.baidu.com"
#     }
# url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn={pageNum}&rn=30&gsm=1e00000000001e&1490169411926="
#
# keword = input("请输入搜索关键字：")
# #转码
# keword = urllib.parse.quote(keword,"utf-8")
#
# n = 0
# j = 0
#
# while (n<3000):
#     error = 0
#     n+=30
#     url1  =url.format(word=keword,pageNum=str(n))
#     #获取请求
#     rep = urllib.request.Request(url1,headers=header)
#     #打开网页
#     rep = urllib.request.urlopen(rep)
#     #获取网页内容
#     try:
#         html = rep.read().decode("utf-8")
#         # print(html)
#     except:
#         print("出错啦！")
#         error = 1
#         print("出错页数："+str(n))
#     if error==1:
#         continue
#     #正则匹配
#     p = re.compile(r"thumbURL.*?\.jpg")
#     #获取正则匹配到的结果，返回list
#     s = p.findall(html)
#     if os.path.isdir(path) !=True:
#         os.makedirs(path)
#     with open("testpic.txt","a") as f:
#         #获取图片
#         for i in s:
#             i = i.replace('thumbURL":"',"")
#             print(i)
#             f.write(i)
#             f.write("\n")
#             #保存图片
#             img_path = os.path.join(path,"pic{num}.jpg".format(num=j))
#             try:
#                 urllib.request.urlretrieve(i, img_path)
#                 j += 1
#                 print(j)
#             except:
#                 continue
#         f.close()
# print("总共爬取的图片数为："+str(j))


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import urllib.request
import uuid

def download_pic(url, name, path):

    if not os.path.exists(path):
        os.makedirs(path)
    res = urllib.request.urlopen(url, timeout=3).read()
    with open(path + name +'.jpg', 'wb') as file:
        file.write(res)
        file.close()

def get_image_url(num, key_word):

    box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    box.send_keys(key_word)
    box.send_keys(Keys.ENTER)
    box = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()

    # 滚动页面
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_elements_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        except:
            pass
        if new_height == last_height:
            # 点击显示更多结果
            try:
                box = driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
            except:
                break
        last_height = new_height

    image_urls = []

    for i in range(1, num):
        try:
            image = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')
            # 此选项为下载缩略图
            # image_src = image.get_attribute("src")
            image.click() # 点开大图
            time.sleep(4)  # 因为谷歌页面是动态加载的，需要给予页面加载时间，否则无法获取原图url，如果你的网络状况一般请适当延长
            # 获取原图的url
            image_real = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img')
            image_url = image_real.get_attribute("src")
            image_urls.append(image_url)
            print(str(i) + ': ' + image_url)
        except:
            print(str(i) + ': error')
            pass
    return image_urls

if __name__ == '__main__':

    # 创建一个参数对象，用来控制chrome是否以无界面模式打开
    ch_op = Options()
    # 设置谷歌浏览器的页面无可视化，如果需要可视化请注释这两行代码
    ch_op.add_argument('--headless')
    ch_op.add_argument('--disable-gpu')

    url = "https://www.google.com/"
    driver = webdriver.Chrome('E:/anaconda/chromedriver.exe', options=ch_op)
    driver.get(url)

    key_word = input('请输入关键词：')
    num = int(input('请输入需要下载的图片数：'))
    _path = input('请输入图片保存路径,例如G:\\\\google\\\\images\\\\ :')

    # path = "G:\\google\\images_download\\" + key_word + "\\"  # 图片保存路径改为自己的路径
    path = _path + key_word + "\\"
    print('正在获取图片url...')
    image_urls = get_image_url(num, key_word)
    for index, url in enumerate(image_urls):
        try:
            print('第' + str(index) + '张图片开始下载...')
            download_pic(url, str(uuid.uuid1()), path)
        except Exception as e:
            print(e)
            print('第' + str(index) + '张图片下载失败')
            continue
    driver.quit()


