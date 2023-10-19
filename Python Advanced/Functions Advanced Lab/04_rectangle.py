def rectangle(length, width):

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle("2", 10))


# Hiding functions parameter behind a nesting.

# def some_funk(page):
#
#     def get_username(username):
#         if username.lower() == "admin":
#             return f"Access to {page} Granted for {username}!"
#         return f"No Access to {page} for {username}!"
#
#     return get_username
#
#
# print(some_funk("whatever")("Admin"))
