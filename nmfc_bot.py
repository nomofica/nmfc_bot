import praw

bot = praw.Reddit(user_agent='nmfc_bot v0.01b',
                  client_id='fsmMzvWLDlHN_w',
                  client_secret='X_Bkx89aoOWkZIMrN9vm9wGmPw4',
                  username='rflightsim',
                  password='qcNsFFCXKYKELJvecjeA')

subreddit = bot.subreddit('nomotest')
comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # fetch body
    author = comment.author # fetch author
    if "what's cooler than being cool?" in text.lower():
        # Generate a message
        message = "ice cold!".format(author)

        comment.reply(message) # send message
