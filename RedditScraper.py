import praw
from datetime import date

file1 = open("sales" + str(date.today()) + ".txt", "a")

reddit = praw.Reddit(client_id="*", client_secret="*", user_agent="PC Sales Bot v1")

subreddit = reddit.subreddit("buildapcsales")

for submission in subreddit.new(limit=25):
    file1.write("Title: " + submission.title + "\n")
    file1.write("Score: " + str(submission.score) + "\n")
    file1.write("URL: " + submission.url + "\n")
    file1.write("------------------------------\n")
    file.write("\n")


file1.close()
