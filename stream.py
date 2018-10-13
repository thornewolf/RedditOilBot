'''
I wanna get the top posts of reddit and log where they were from so they can be reposted later.
Is that too much to ask?
'''

import praw
import string
import time
from Config import CredentialsReddit as cr
import json
import datetime
import re
import random


reddit = praw.Reddit(user_agent = cr.user_agent, # A brief description of your bot! <#
                 client_id = cr.client_id,# Your API public key
                 client_secret = cr.client_secret,
                 username = cr.username,
                 password = cr.password)



for comment in reddit.subreddit('all').stream.comments():
    b = comment.body
    r = re.compile('[^oil]*?o[^oil]*?i[^oil]*?l[0-9a-zA-Z.!?]*')
    f = r.search(b)
    
    if f:
        stm = f.group(0)
        if len(stm)<10:
            if random.random()<0.55:
                for i in 'oil':
                    stm = stm.replace(i,'**'+i+'**',1)
                    result = f'''>{f.group(0)}
            
            
>{stm}
            
[OIL](https://www.globalresearch.ca/wp-content/uploads/2015/04/soldiers-oil-400x208.jpg)'''
                    print(result)
                    print()
                    comment.reply(result)
            