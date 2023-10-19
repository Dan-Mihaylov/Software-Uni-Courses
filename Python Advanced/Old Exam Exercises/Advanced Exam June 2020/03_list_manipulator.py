def list_manipulator(nums: list, *args):
    command, where, *what = args

    if command == "add":
        if where == "beginning":
            while what:
                nums.insert(0, what.pop())
        else:
            nums.extend(what)

    elif command == "remove":
        if where == "beginning":
            if what:
                nums = nums[what.pop():]
            else:
                nums.pop(0)

        else:
            if what:
                nums = nums[: len(nums) - what.pop()]
            else:
                nums.pop()

    return nums











print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))