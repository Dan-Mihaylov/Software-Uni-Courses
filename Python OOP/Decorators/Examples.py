"""
You will create a function that receives a list with tasks [strings] and will return whether they have been completed
based on the len(task).

Then you will create a decorator, creator function, get_bonus(number), that will receive the number of the bonus you are
getting, and in the decorator functions wrapper, you will check the condition, that you have completed at least 4 tasks
to get the bonus.

"""

from functools import wraps


def get_bonus(number):

    def decorator(function):

        @wraps(function)
        def wrapper(tasks_completed: list):
            result = function(tasks_completed)
            points = len(result) * 10

            if len(result) > 3:
                return points + number

            return points

        return wrapper

    return decorator


@get_bonus(10)
def check_completed_tasks(tasks: list):
    """
    This function checks if you have completed the tasks, based on the condition that the len(task) is greater than 3
    :param tasks: List, with the names of the tasks
    :return: List with completed tasks
    """
    return [x for x in tasks if len(x) > 3]


print(check_completed_tasks(["study", "nope", "som", "no", "good"]))
print(check_completed_tasks.__doc__)

