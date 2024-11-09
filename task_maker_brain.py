import json
import time
from uuid import uuid4


def find_index(seq: list[dict], key: str, value):
    for i, dictionary in enumerate(seq):
        if dictionary[key] == value:
            return i
    raise ValueError(f'element with {key} "{value}" not found')


class Task:
    """dataclass for a task"""

    def __init__(self, title: str):
        self.title: str = title
        self.created_at: int = int(time.time())
        self.completed: bool = False
        self.id: str = str(uuid4())


class TaskManager:
    def __init__(self):
        self.file = '.tasks.json'
        self.completed_file = '.completed_tasks.json'

    def get_tasks(self, completed: bool = False):
        file = self.file if not completed else self.completed_file
        with open(file, 'r') as f:
            try:
                tasks = json.load(f)
            except json.JSONDecodeError:
                tasks = []
            return tasks

    def update_tasks(self, tasks: json, completed: bool = False):
        file = self.file if not completed else self.completed_file
        with open(file, 'w') as f:
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

    def delete(self, task_id: str = None, task_title: str = None):
        if not task_id and not task_title:
            raise TypeError('None task id or task title given')
        tasks = self.get_tasks()

        if task_id:
            index = find_index(tasks, 'id', task_id)
        elif task_title:
            index = find_index(tasks, 'title', task_title)
        else:
            index = None

        tasks.pop(index)
        self.update_tasks(tasks)

    def complete(self, task_id: str = None, task_title: str = None):
        if not task_id and not task_title:
            raise TypeError('None task id or task title given')
        tasks = self.get_tasks()

        if task_id:
            index = find_index(tasks, 'id', task_id)
        elif task_title:
            index = find_index(tasks, 'title', task_title)
        else:
            index = None

        tasks[index]['completed'] = True
        completed_task = tasks.pop(index)

        try:
            completed_tasks = self.get_tasks(completed=True)
        except (FileNotFoundError, json.JSONDecodeError):
            completed_tasks = []
        completed_tasks.append(completed_task)

        self.update_tasks(tasks)
        self.update_tasks(completed_tasks, completed=True)


if __name__ == '__main__':
    testing_task_manager = TaskManager()
    testing_task_manager.complete(task_title='test task')
