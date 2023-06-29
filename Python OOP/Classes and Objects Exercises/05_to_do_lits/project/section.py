from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task_info in self.tasks:
            if task_info.name == task_name:
                task_info.completed = True

                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                count += 1
        return f"Cleared {count} tasks."

    def view_section(self):

        result = [f"Section {self.name}:"]

        for task in self.tasks:
            result.append(task.details())

        return f"\n".join(result)




