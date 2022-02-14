import tweepy
import pdfplumber
import random
import os
import re
from datetime import datetime


directory = ''  #path to the folder containing the books/pdfs you want to tweet 

# your own twitter access keys & tokens
API_key = ""
API_key_secret = ""
bearer_token = ""
access_token = ""
access_secret = ""

#creation of twitter object API v2
client = tweepy.Client(bearer_token, API_key, API_key_secret, access_token, access_secret, wait_on_rate_limit=False)

#check time
time = datetime.now()
hour = time.hour

#at midnight, randomly selects a sentence from a book/pdf and tweets the sentence + title of book/pdf
if hour == 0:
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.pdf'):
            with pdfplumber.open(directory + file) as pdf:
                pg_num = random.randint(0, len(pdf.pages))
                page = pdf.pages[pg_num]
                text = page.extract_text()
                sentences = text.split('.')
                s_num = random.randint(0, len(sentences))
                twee = re.sub('\r?\n?', '', sentences[s_num])
                tweet = re.sub('-', '', twee)
                title = filename.split('.')
                tweet1 = (tweet + '.\n' + '- ' + title[0].capitalize())
                try:
                    client.create_tweet(text= tweet1)
                except:
                    client.create_tweet(text= tweet1)