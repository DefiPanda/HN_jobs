import urllib
import urllib2
import re, sys
import smtplib
import os
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
  aResp = urllib2.urlopen(url);
  web_pg = aResp.read();
  return web_pg

def findAllEmails(content):
  email_pattern = re.compile('([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)')
  all_emails = []
  for match in email_pattern.findall(content):
    all_emails.append(match[0])
  return all_emails

def processRequests(urls):
  all_emails = []
  for url in urls:
    content = Connect2Web(url)
    all_emails.extend(findAllEmails(content))
  return all_emails

def main():
  urls = ["https://news.ycombinator.com/item?id=5637663","https://news.ycombinator.com/item?id=5472746","https://news.ycombinator.com/item?id=5304169"]
  starting_url_index = 1
  if(len(sys.argv) >2 and sys.argv[1] == '-send'):
    starting_url_index = 7
  for arg in sys.argv[starting_url_index:]:
    urls.append(arg)
  all_emails = processRequests(urls)
  if(len(sys.argv) >2 and sys.argv[1] == '-send'):
    send_mail(sys.argv[2], sys.argv[3], all_emails, sys.argv[4], sys.argv[5], files=[sys.argv[6]])
  else:
    print all_emails

if __name__ == '__main__':
    main()
