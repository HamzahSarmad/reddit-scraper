import praw
import pandas as pd
from datetime import date

file1 = open("C:/Users/Hamzah/Documents/PCPARTS/sales " + str(date.today()) + ".txt", "a")

reddit = praw.Reddit(client_id="tWUMVBRDkwnINg", client_secret="86lXP8obaXswzUM8jy-OfUKNaXk", user_agent="PC Sales Bot v1")

subreddit = reddit.subreddit("buildapcsales")

for submission in subreddit.new(limit=25):
    file1.write("Title: " + submission.title + "\n")
    file1.write("Text: " + submission.selftext + "\n")
    file1.write("Score: " + str(submission.score) + "\n")
    file1.write("URL: " + submission.url + "\n")
    file1.write("\n")


file1.close()