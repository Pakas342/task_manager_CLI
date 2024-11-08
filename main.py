from argparse import ArgumentParser

parser = ArgumentParser(
    prog='TaskManager',
    description='Task Manager for adding, removing and editing tasks on the current project'
)

parser.add_argument('action', choices=['add', 'delete', 'complete', 'read'])
parser.add_argument('--i', '--id')
parser.add_argument('--all', '-a')
parser.add_argument('--t', '-title')
parser.add_argument('--c', '-complete', action='store_true')
parser.add_argument('--d', '-delete', action='store_true')

args = parser.parse_args()

if args.action == 'add':
