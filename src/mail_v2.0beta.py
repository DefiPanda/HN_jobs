import urllib2, re, sys, smtplib, os, time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def send_mail(send_from, password, send_to, subject, text, files=[]):
  assert type(send_to)==list
  assert type(files)==list

  msg = MIMEMultipart()
  msg['From'] = send_from
  msg['To'] = COMMASPACE.join(send_to)
  msg['Date'] = formatdate(localtime=True)
  msg['Subject'] = subject

  msg.attach( MIMEText(text) )

  for f in files:
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(f,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)

  smtpserver = smtplib.SMTP("smtp.gmail.com", 587, timeout=30)
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo
  smtpserver.login(send_from, password)
  smtpserver.sendmail(send_from, send_to, msg.as_string())
  smtpserver.close()

def Connect2Web(url):
  #in case of HN blocks IP, it will be on this proxy rather than your IP. So it protects you from being block from HN.
  proxy  = urllib2.ProxyHandler({'https': '66.42.224.222:3129'})
  #slept 5 seconds to avoid server IP block
  time.sleep(5)
  opener = urllib2.build_opener(proxy)
  urllib2.install_opener(opener)
  # fake HTTP headers so our program will not be recognized as a spider
  headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
  }
  req = urllib2.Request(
    url = url,
    headers = headers
  )
  aResp = urllib2.urlopen(req)
  web_pg = aResp.read()
  return web_pg

def findAllEmails(content):
  email_pattern = re.compile('([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)')
  all_emails = []
  for match in email_pattern.findall(content):
    all_emails.append(match[0])
  return all_emails

def findAllHttpsLinks(content):
  url_pattern = re.compile('item\?id=\d{7}')
  all_urls = []
  for match in url_pattern.findall(content):
    if 'https://news.ycombinator.com/' + match not in all_urls:
      all_urls.append('https://news.ycombinator.com/' + match)
  return all_urls

def processRequests():
  all_emails = []
  for url in searchURLs():
    content = Connect2Web(url)
    email = findAllEmails(content)
    all_emails.extend(email)
  return all_emails

def searchURLs():
  web_pg = Connect2Web('https://news.ycombinator.com/submitted?id=whoishiring')
  return findAllHttpsLinks(web_pg)

def main():
  all_emails = processRequests()
  if(len(sys.argv) >2 and sys.argv[1] == '-send'):
    send_mail(sys.argv[2], sys.argv[3], all_emails, sys.argv[4], sys.argv[5], files=[sys.argv[6]])
  print all_emails

if __name__ == '__main__':
    main()
