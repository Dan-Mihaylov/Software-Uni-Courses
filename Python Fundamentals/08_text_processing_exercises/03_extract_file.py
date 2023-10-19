file_path = input().split('\\')

for word in file_path:
    if "." in word:
        name, extension = word.split(".")
        print(f"File name: {name}")
        print(f"File extension: {extension}")
        break
