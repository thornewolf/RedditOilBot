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

DAY_LEN = 1000*60*60*24
def getDaysTopPosts(subreddits=['all'],n=5):
	subreddits = '+'.join(subreddits)
	print("[i] Getting Top posts for {} @ {}".format(subreddits,datetime.datetime.fromtimestamp(time.time())))
	reddit = praw.Reddit(user_agent = cr.user_agent, # A brief description of your bot! <#
	                         client_id = cr.client_id,# Your API public key
	                         client_secret = cr.client_secret,
	                         username = cr.username,
	                         password = cr.password)

	
	subreddit = reddit.subreddit(subreddits)
	#print(help(subreddit))



	submissions = []
	for submission in subreddit.top('day',limit=n):
		t = int(submission.created)
		t = datetime.datetime.fromtimestamp(t)
		t = [t.year,t.month,t.day]
		j = {'title':submission.title,
		'score':submission.score,'url':submission.url,
		'selftext':submission.selftext,'created':t,'subreddit':submission.subreddit.display_name}
		submissions.append(j)
	print('[:] Got top posts')
	return submissions #list object
def loadPostListToFile(lst,fileName):
	try:
		with open(fileName,'r+') as f:
			r = f.read()
			if len(r) > 3:
				r = json.loads(r)
				for i in r:
					lst.append(i)
	except:
		pass
	with open(fileName,'w+') as f:
		s = json.dumps(lst)
		f.write(s)
	return 1
def makeRedditPost(post)
r = getDaysTopPosts(subreddits=['askreddit','pics'],n=5)
loadPostListToFile(r,"txt.json")