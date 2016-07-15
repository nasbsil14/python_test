from html.parser import HTMLParser
from lxml import etree, html
from io import StringIO, BytesIO
from lxml.builder import E

class MyHTMLParser(HTMLParser):
    buff = list()
    def __init__(self):
        HTMLParser.__init__(self, convert_charrefs=False)
        self.fed = []
    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        for name, value in attrs:
            #print(attr)
            if name == 'value':
                #print(value)
                self.buff.append(value)
#    def handle_endtag(self, tag):
#        print("Encountered an end tag :", tag)
#    def handle_data(self, data):
#        print("Encountered some data  :", data)
    def getBuff(self):
        return self.buff

#parser = MyHTMLParser()
parser = etree.HTMLParser(encoding='utf-8')

#f = open(r'C:\workspace\test\test.xhtml', 'r', encoding='utf_8_sig')
#data = f.read()
#f.close()
#print(data.encode('utf_8_sig'))

#with open(r'C:\workspace\test\test.xhtml', 'r', encoding='utf_8_sig') as html:
    #print(html)
    #parser.feed(html)
    #print(parser.getBuff())

#with open(r'C:\workspace\test\test.xhtml', 'r', encoding='utf_8_sig') as html:
#    data = f.read()
    #doc = lxml.html.document_fromstring(data)
    #tree = etree.parse(html, parser)
    #tree = etree.parse(html)
    #print(etree.tostring(tree, pretty_print=True, encoding='UTF-8'))

#htmlエンコードされた文字(&nbspとか)は処理できないらしい・・・なのでlxml.htmlを使う。
#tree = etree.parse(r'C:\workspace\test\test.xhtml')
#print(etree.tostring(tree, pretty_print=True, encoding='UTF-8'))
htmldata = html.parse(r'C:\workspace\test\test.xhtml')
print(html.tostring(htmldata))
