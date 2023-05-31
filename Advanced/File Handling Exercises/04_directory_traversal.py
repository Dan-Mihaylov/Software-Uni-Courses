import os


def save_extensions(dir_name, depth = 0):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)    # take the full path
        # print(file)

        if os.path.isfile(file):
            extension = file_name.split(".")[-1]    # take the last item in list, which is the extension

            if not extension in extensions:
                extensions[extension] = []

            extensions[extension].append(file_name)

        elif os.path.isdir(file):
            if depth < 2:
                save_extensions(file, depth + 1)
            else:
                break


directory = input()
extensions = {}
result = []
save_extensions(directory)
extensions = dict(sorted(extensions.items(), key=lambda x: x[0]))

for ext, files in extensions.items():
    result.append(f"{ext}")
    [result.append(f"- - - {file}") for file in sorted(files)]

with open("files/reported.txt", "w") as report_file:
    report_file.write('\n'.join(result))


