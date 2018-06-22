from urllib import request
import re

class Spider():
    url = 'http://www.panda.tv/cate/lol'
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls


    def __analysis(self, htmls):
        root_pattern = '<div class="video-info">(.*?)</div>'
        name_pattern = '</i>(.*?)</span>'
        number_pattern = '<span class="video-number">(.*?)</span>'
        #re.compile(root_pattern, htmls)
        root_htmls = re.findall(root_pattern, htmls, re.S)
        anchors = []
        for html in root_htmls:
            name = re.findall(name_pattern, html, re.S)
            number = re.findall(number_pattern, html, re.S)
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
        return anchors

    def __refine(self, anchors):
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
                  }
        return map(l, anchors)

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank    ' + str(rank + 1)
                  + '  :  ' + anchors[rank]['name']
                  + '    ' + anchors[rank]['number'])

    def __sort_seed(self,anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        anchors = self.__show(anchors)
        print(anchors)


spider = Spider()
spider.go()