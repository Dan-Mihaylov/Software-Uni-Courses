class Comment:

    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user1", "I like this book", 100)
print(comment.username)
print(comment.content)
print(comment.likes)
print()

new_comment = Comment("Daniel", "I don't like this book", 2)
print(new_comment.username)
print(new_comment.content)
print(new_comment.likes)