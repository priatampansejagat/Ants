from selenium import webdriver as wd

class Browse:


    driver = None
    url = None
    content = None


    def set_url(self,url):
        self.url = url
        print('url confimed = ' + str(self.url))

    def get_url(self):
        return self.url

    def get_page_content(self):
        self.content = self.driver.page_source
        # print('page source = \n'+ self.content)
        return self.content

    def start(self):
        print('execute: Browsing')
        option = wd.ChromeOptions()
        # option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-dev-sh-usage')

        self.driver = wd.Chrome(options=option)
        self.driver.get(str(self.url))