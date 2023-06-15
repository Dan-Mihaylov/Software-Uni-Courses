x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print(f"outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)


