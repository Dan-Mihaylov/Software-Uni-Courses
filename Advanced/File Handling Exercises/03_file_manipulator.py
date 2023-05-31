import os


def add(file_, info):
    with open(f"files/{file_}", "a") as file:
        file.write(f"{info}\n")


def create(file_):
    with open("files/file_", "w") as file:
        pass


def replace(file_, old_string, new_string):
    try:
        new_text = ""

        with open(f"files/{file_}", "r+") as file:
            text = file.read()
            text = text.replace(old_string, new_string)
            new_text = text

        os.remove(f"files/{file_}")        # file_.seek doesn't work, it leaves random letters in.
        new_file = open(f"files/{file_}", "w")
        new_file.write(new_text)

    except FileNotFoundError:
        print(f"An error occurred")


def delete(file_):
    try:
        os.remove(f"files/{file_}")
    except FileNotFoundError:
        print(f"An error occurred")


commands = {
    "Create": create,
    "Add": add,
    "Replace": replace,
    "Delete": delete,
}

while True:
    command, *info = input().split("-")

    if command == "End":
        break

    commands[command](*info)


