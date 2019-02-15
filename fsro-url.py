import requests,re,os
class Movie_link:
    def __init__(self):
        pass
        
    def pages_num(self,url):
        self.content = self.content_web(url)
        self.pa=r'<span title="共 (.*?) 页"> / .*? 页</span>'
        self.page=re.findall(self.pa,self.content)
        return self.page[0]
    def single_page(self):
        pass
    def multiple_page(self):
        pass    
    def content_web(self,url):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
        req = requests.get(url,headers=self.headers)
        html=req.text
        return html
    def save_content(self):
        pass

def main():
    url2="http://www.fsro.cn/plugin.php?id=xlwsq_ysdp&fl=3&yy=5&page=1"
    movie=Movie_link()
    a=movie.pages_num(url2)
    print(a)

if __name__ == '__main__':
    main()
