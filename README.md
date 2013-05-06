HN_jobs
=======

HN_job is a python script to post your job application to all opening listed in HN who's hiring and more.  
  
By default it will return all the emails you can apply job to listed in HN who's hiring March, April and May 2013. You can add additional urls you would like HN_jobs to search for you as parameters at the end of command  

Usage:  
python mail.py [optional -send your_email your_password email_title email_body your_resume_title] [optional additional urls]  

Example:  
python mail.py   
python mail.py https://news.ycombinator.com/item?id=3537881 https://news.ycombinator.com/item?id=2270790  
python mail.py -send email@gmail.com passwd "Jack's Test Title" "Hey, could you please read my resume" "test.pdf"  
  
without "-send" parameters, HN_jobs will just print out an array of emails mined at the urls we searched. For example, when you type "python mail.py", you will get following screenshot:  
![ScreenShot](https://github.com/jw2013/HN_jobs/blob/master/screenshot.png)
  
  
Happy job hunting!
