from bs4 import *

class Parser:

    soup = None
    page_content=None

    def __init__(self,page_content=None):
        self.page_content=page_content


    def set_page_content(self,page_content):
        self.page_content = page_content
        # print('parser content = ' + self.page_content)


    def content_builder(self,tags):

        result = ''
        for tag in tags:
            result = result + '\n' + str(tag)

        return result

    def scrape(self,rules):
        print('execute: Extracting')
        # print(rules)

        final_result = {}
        count = 0

        self.soup = BeautifulSoup(self.page_content, 'html.parser')

        final_result[count]=self.soup

        for rule in rules:

            # translating rules, mana elemen dan mana atribut
            rule_split= rule.split('=')
            elements = str(rule_split[0]) if len(rule_split)>0 else None
            attrs = rule_split[1].split(',') if len(rule_split)>1 else None

            # format atribut menjadi dictionary
            attr_build = {}
            if attrs != None:
                for attr in attrs:
                    temp_attr=attr.split(':')
                    attr_build[str(temp_attr[0])] = str(temp_attr[1])
            else:
                pass

            # scrape
            result_array = final_result[count].findAll(elements, attr_build)

            # save the result and prepare for next rules
            count = count+1
            final_result[count] = BeautifulSoup(self.content_builder(result_array), 'html.parser')


            """
            cari solusi untuk get valuenya atribut dengan format rules tertentu, misal td=class
            """




        # print('final result = \n {}'.format(final_result[count]))

        # self.output_builder(final_result)
        return final_result

    # def output_builder(self,result):
    #     pass


