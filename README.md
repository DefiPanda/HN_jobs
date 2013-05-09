HN_jobs
=======

Copyright (c) 2013 Jack Wang  
  
What is HN_jobs?
-------------  
HN_job is a python script to post your job application to all opening listed in HN who's hiring and more.  
  
By default mail.py will return all the emails you can apply job to listed in HN who's hiring March, April and May 2013. You can add additional urls you would like HN_jobs to search for you as parameters at the end of command.  
**mail_v2.0beta.py will by default search all the posts listed on the first submission page of HN user whoishiring, so you will automatically get all the recent job posting emails if you use mail_v2.0beta.py.  


Usage  
-------------  
python mail.py [optional -send your_email your_password email_title email_body your_resume_title] [optional additional urls]  

Example:  
python mail.py   
python mail.py https://news.ycombinator.com/item?id=3537881 https://news.ycombinator.com/item?id=2270790  
python mail.py -send email@gmail.com passwd "Jack's Test Title" "Hey, could you please read my resume" "test.pdf"  
  
without "-send" parameters, HN_jobs will just print out an array of emails mined at the urls we searched. For example, when you type "python mail.py", you will get following screenshot:  
  
![ScreenShot](https://raw.github.com/jw2013/HN_jobs/master/screenshot/screenshot.png)
  
  
Usage of v2.0
-------------  
python mail_v2.0beta.py [optional -send your_email your_password email_title email_body your_resume_title]  
Example:  
python mail_v2.0beta.py  
python mail_v2.0beta.py -send email@gmail.com passwd "Jack's Test Title" "Hey, could you please read my resume" "test.pdf"  
  
without "-send" parameters, HN_jobs will just print out an array of emails mined at the urls we searched (all recent HN who's hiring posts). For example, when you type "python mail.py", you will get result located at:  
[a link](https://raw.github.com/jw2013/HN_jobs/master/test_result/mail_v2.0beta_result.txt)  

  
Happy job hunting!  
=======
