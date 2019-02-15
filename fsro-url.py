import requests,re,os
class Movie_link:
    def __init__(self):
        pass
    # 获取总页数   
    def pages_num(self,url):
        self.content = self.content_web(url)
        self.pa=r'<span title="共 (.*?) 页"> / .*? 页</span>'
        self.page=re.findall(self.pa,self.content)
        return self.page[0]
    
    # 获取单页连接地址
    def single_page(self,url):
        self.content= self.content_web(url)
        self.li=r'<a href="(.*?)" target=\'_blank\'>'
        self.link=re.findall(self.li,self.content)
        for i in self.link:
            print("http://www.fsro.cn/"+i)
        return  self.link
    # 获取多页连接地址
    def multiple_page(self,url):
        self.page=int(self.pages_num(url))
        for i in range(self.page+1):
            url = url+str(i+1)
            self.single_page(url)

    # 获取网页内容
    def content_web(self,url):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
        req = requests.get(url,headers=self.headers)
        html=req.text
        return html
    def save_content(self):
        pass

def main():
    url="http://www.fsro.cn/forum-129-1.html"
    url2="http://www.fsro.cn/plugin.php?id=xlwsq_ysdp&fl=3&yy=5&page="
    movie=Movie_link()
    a=movie.pages_num(url)
    b=movie.multiple_page(url2)
    print(b)

if __name__ == '__main__':
    main()
