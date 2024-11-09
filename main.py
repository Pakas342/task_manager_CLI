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

if args.action == 'add':
    try:
        title = args.title
        task_manager.add(title)
    except Exception as e:
        print(e)


