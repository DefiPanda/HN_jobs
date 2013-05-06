import urllib
import urllib2
import re, sys

def Connect2Web(url):
  aResp = urllib2.urlopen(url);
  web_pg = aResp.read();
  return web_pg

def findAllEmails(content):
  email_pattern = re.compile('([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)')
  for match in email_pattern.findall(content):
    print match[0]

def processRequests(urls):
  for url in urls:
    content = Connect2Web(url)
    findAllEmails(content)

def main():
  urls = ["https://news.ycombinator.com/item?id=5637663","https://news.ycombinator.com/item?id=5472746","https://news.ycombinator.com/item?id=5304169"]
  for arg in sys.argv[1:]:
  	urls.append(arg)
  processRequests(urls)

if __name__ == '__main__':
    main()