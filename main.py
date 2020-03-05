import praw

reddit = praw.Reddit()

#print(reddit.user.me())
subreddit = reddit.subreddit("dataisbeautiful")

comments = []
def clean(t):
	return "".join([c for c in t if c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ?!"])

for submission in subreddit.hot(limit=25):

	print(submission.title)

	prepared = []

	submission.comments.replace_more(None)

	for i, tlc in enumerate(submission.comments):
		prepared.append([f"/{clean(submission.title)}/{clean(tlc.body)[:25]}", tlc])#f"/{i}"
		
	while len(prepared) > 0:
		comment = prepared.pop(0)
		comments.append(comment)
		comment[1].replies.replace_more(None)
		for ci, child in enumerate(comment[1].replies):
			prepared.append([comment[0] + f"/{clean(child.body)[:25]}", child])#+ f"/{ci}"

def color(score):
	if score == 1:
		return "#ffffff"
	elif score < 1:
		return "#0000ff"
	else:
		return "#ff0000"

lines = ""

for (path, comment) in sorted(comments, key=lambda c:c[1].created_utc):
	if comment.author:
		lines += f"{int(comment.created_utc)}|{comment.author.name}|A|{path}|{color(comment.score)}\n"
	else:
		#print("NO AUTHOR:", comment.body)
		#[deleted]
		pass

gfname = "combined.txt"

gf = open(gfname, "w+")
gf.write(lines)
gf.close()

import os
os.system("gource combined.txt")
