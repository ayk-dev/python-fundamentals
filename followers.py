followers_likes= {}
followers_comments= {}

while True:
    line = input()
    if line == 'Log out':
        break

    args = line.split(': ')
    command= args[0]
    username = args[1]

    if command == 'New follower':
        if username not in followers_likes and username not in followers_comments:
            followers_comments[username] = 0
            followers_likes[username] = 0

    elif command == 'Like':
        count = int(args[2])
        if username not in followers_likes and username not in followers_comments:
            followers_comments[username] = 0
            followers_likes[username] = 0
        followers_likes[username] += count

    elif command == 'Comment':
        count = 1
        if username not in followers_comments and username not in followers_likes:
            followers_comments[username] = count
            followers_likes[username] = 0
        else:
            followers_comments[username] += count

    elif command == 'Blocked':
        if username in followers_comments and username in followers_likes:
            followers_comments.pop(username)
            followers_likes.pop(username)
        else:
            print(f"{username} doesn't exist.")

count_followers = len(followers_likes.keys())
print(f'{count_followers} followers')

sorted_followers = dict(sorted(followers_likes.items(), key=lambda x: (-x[1], x[0])))
for k, v in sorted_followers.items():
    print(f'{k}: {v + followers_comments[k]}')