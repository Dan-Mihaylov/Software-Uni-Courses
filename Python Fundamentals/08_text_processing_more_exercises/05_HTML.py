title = input()
article = input()

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {article}\n</article>")

line = input()

while line != "end of comments":
    print(f"<div>\n    {line}\n</div>")
    line = input()
