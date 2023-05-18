from bs4 import *

class Parser:

    soup = None
    page_content=None

    def __init__(self,page_content=None):
        self.page_content=page_content


    def set_page_content(self,page_content):
        self.page_content = page_content
        # print('parser content = ' + self.page_content)

    def scrape(self,rules):
        print('execute: Extracting')
        # print(rules)

        self.soup = BeautifulSoup(self.page_content, 'html.parser')

        for rule in rules:
            # print(rule)

            rule_split= rule.split('=')
            elements = str(rule_split[0]) if len(rule_split)>0 else None
            attrs = rule_split[1].split(',') if len(rule_split)>1 else None

            # do Scrape
            if attrs != None:

                attr_build={}

                for attr in attrs:
                    temp_attr=attr.split(':')
                    attr_build[str(temp_attr[0])] = str(temp_attr[1])

                result_array = self.soup.findAll(elements, attr_build)

                for result_elements in result_array:
                    print('result = \n{}'.format(result_elements) )


            else:
                pass


        return True




