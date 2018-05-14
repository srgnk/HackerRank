from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
