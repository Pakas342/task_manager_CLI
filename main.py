from argparse import ArgumentParser

from task_maker_brain import TaskManager

parser = ArgumentParser(
    prog='TaskManager',
    description='Task Manager for adding, removing and editing tasks on the current project'
)

task_manager = TaskManager()

parser.add_argument('action', choices=['add', 'delete', 'complete', 'read'])
parser.add_argument('-i', '--id')
parser.add_argument('-a', '--all')
parser.add_argument('-t', '--title')
parser.add_argument('-c', '--complete', action='store_true')
parser.add_argument('-d', '--delete', action='store_true')

args = parser.parse_args()

action = args.action

match action:

    case 'add':
        try:
            title = args.title
            task_manager.add(title)
        except Exception as e:
            print(e)

    case 'delete':
        title, task_id = args.title, args.id
        if not title and not task_id:
            print('Please provide at least a --title, or an --id')
        if task_id:
            try:
                task_manager.delete(task_id=task_id)
            except Exception as e:
                print(e)
        if title:
            try:
                task_manager.delete(task_title=title)
            except Exception as e:
                print(e)

    case 'complete':
        title, task_id = args.title, args.id
        if not title and not task_id:
            print('Please provide at least a --title, or an --id')
        if task_id:
            try:
                task_manager.complete(task_id=task_id)
            except Exception as e:
                print(e)
        if title:
            try:
                task_manager.complete(task_title=title)
            except Exception as e:
                print(e)
