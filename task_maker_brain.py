import json
import time
from uuid import uuid4


def find_index(seq: list[dict], key: str, value):
    for i, dictionary in enumerate(seq):
        if dictionary[key] == value:
            return i
    raise ValueError(f'element with {key} "{value}" not found')


class Task:
    """Class for a task"""
    def __init__(self, title: str):
        self.title: str = title
        self.created_at: int = int(time.time())
        self.completed: bool = False
        self.id: str = str(uuid4())


class TaskManager:
    def __init__(self):
        self.file = '.tasks.json'

    def get_tasks(self):
        with open(self.file, 'r') as f:
            try:
                tasks = json.load(f)
            except json.JSONDecodeError:
                tasks = []
            return tasks

    def update_tasks(self, tasks: json):
        with open(self.file, 'w') as f:
            json.dump(tasks, f)

    def add(self, task_title):
        if not task_title:
            raise TypeError('None task title given')
        tasks = self.get_tasks()

        # Done with a set {} instead of a list to achieve O(1)
        title_list = {task['title'] for task in tasks} if tasks else {}
        if task_title in title_list:
            raise Exception('Already Existing Task')

        new_task = Task(task_title)
        tasks.append(new_task.__dict__)

        self.update_tasks(tasks)

    def delete_by_id(self, task_id: str):
        if not task_id:
            raise TypeError('None task_id given')
        tasks = self.get_tasks()
        index = find_index(tasks, 'id', task_id)
        tasks.pop(index)
        self.update_tasks(tasks)

    def delete_by_title(self, task_title: str):
        if not task_title:
            raise TypeError('None task_title given')
        tasks = self.get_tasks()
        index = find_index(tasks, 'title', task_title)
        tasks.pop(index)
        self.update_tasks(tasks)


if __name__ == '__main__':
    testing_task_manager = TaskManager()
    # testing_task_manager.add("test task")
    testing_task_manager.delete_by_title("test task")
