"""
Create a task list, allowing the user to
add, undo and redo items to the list.

Commands:
(List, Undo, Redo, Clear and Exit)
"""

import os
import sys
import json

this_file_path = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = file_path = f'{this_file_path}/data/task_list.json'

def clear():
    os.system("clear")

def list_tasks(task_list: list):
    clear()
    print("TASKS:\n------")
    print(*task_list, sep="\n", end="\n"*2)

def add_task(task: str, task_list: list):
    clear()
    task_list.append(task)
    print('\nTask created!', end='\n'*2)

def undo_task(task_list: list, cache_list: list):
    clear()
    if len(task_list) > 0:
        task_removed = task_list.pop()
        cache_list.append(task_removed)
    else:
        print('Nothing to undo/redo.', end='\n'*2)

def exit_app():
    clear()
    sys.exit()

def save_tasks(task_list: list, try_to_open: bool = False):
    clear()

    with open(FILE_PATH, 'w', encoding='utf8') as file:
        json.dump(task_list, file, indent=2, ensure_ascii=False)

    if try_to_open:
        print(f'A new file was opened.', end='\n'*2)
    else:
        print(f'File saved at: {file_path}.', end='\n'*2)

def open_task_list(task_list: list, cache_list: list):
    clear()

    cache_list.clear()
    task_list.clear()

    try:
        with open(FILE_PATH, 'r', encoding='utf8') as file:
            task_list.extend(json.load(file))
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            save_tasks(task_list, True)
        else:
            print(e)

welcome_message = "Welcome to Task List V0.0.1!\n\nType one of the commands or start\ntyping your task to create a list\n"

def task():

    tasks = []
    cache = []

    print(welcome_message)
    
    while True:
        print("-"*61)
        print("Commands: | list | undo | redo | exit | clear | save | open |")
        print("-"*61, end='\n'*2)

        input_task = input('Command or Task: ').lower()

        commands = {
            'list': lambda: list_tasks(tasks),
            'undo': lambda: undo_task(tasks, cache),
            'redo': lambda: undo_task(cache, tasks),
            'exit': lambda: exit_app(),
            'clear': lambda: clear(),
            'save': lambda: save_tasks(tasks),
            'open': lambda: open_task_list(tasks, cache),
        }

        commands[input_task]() if commands.get(input_task) is not None else add_task(input_task, tasks)

task()
