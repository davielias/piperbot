import praw
import config
import os

REPLY_MESSAGE = "Middle out? Did you know that Pied Piper is the pioneering middle out compression platform. " \
                "Using middle out compression, we were able to take your files and make them smaller. " \
                "A lot smaller. To even less than a quarter of their original size! We even won at TechCrunch " \
                "Disrupt! " \
                "Come check us out over at [/r/SilliconValley](https://www.reddit.com/r/SiliconValleyHBO/)." \
                " " \
                " " \
                " " \
                "I am a bot! I am based off of [/u/busterroni](https://www.reddit.com/user/busterroni)'s bot " \
                "tutorial," \
                " but I am maintained and created by [/u/therealmandusa](https://www.reddit.com/user/therealmandusa)"


def authenticate():
    reddit = praw.Reddit(username = config.username,
                         password = config.password,
                         client_id = config.client_id,
                         client_secret = config.client_secret,
                         user_agent="middle_out_bot's Pied Piper pitch! v0.1!")
    print("Authenticated bruh!")
    return reddit


def run_bot(reddit, comments_replied_to):
    print("Gonna grab 25 comments, hope you don't mind.")

    for comment in reddit.subreddit('test').comments(limit=25):
        if "middle out" in comment.body and comment.id not in comments_replied_to \
                    and comment.author != reddit.user.me():
            print("Looking for comments with the phrase \"middle out\" in them. Found one! It's comment " + comment.id)
            comment.reply(REPLY_MESSAGE)
            print("So I replied to comment " + comment.id)

            comments_replied_to.append(comment.id)

    print(comments_replied_to)


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as doc:
            comments_replied_to = doc.read()
            comments_replied_to = comments_replied_to.split("\n")

    return comments_replied_to


def main():
    reddit = authenticate()
    comments_replied_to = get_saved_comments()
    # while True:
    run_bot(reddit, comments_replied_to)

if __name__ == '__main__':
    main()

