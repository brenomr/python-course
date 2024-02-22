"""
Create a task list, allowing the user to
add, undo and redo items to the list.

Commands:
(List, Undo, Redo, Clear and Exit)
"""

import os
import sys
import json

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

def save_tasks(task_list: list):
    clear()

    if len(task_list) == 0:
        print('Task list empty, nothing was saved!', end='\n'*2)
        return

    this_file_path = os.path.dirname(os.path.realpath(__file__))
    file_path = f'{this_file_path}/data/task_list.json'
    
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(task_list, file, indent=2, ensure_ascii=False)
        print(f'File saved at: {file_path}.', end='\n'*2)

def open_task_list(task_list: list, cache_list: list):
    clear()

    if len(task_list) > 0:
        print('You already have a list, try removing all items before opening an existing list!', end='\n'*2)
        return
    
    cache_list.clear()

    this_file_path = os.path.dirname(os.path.realpath(__file__))
    file_path = f'{this_file_path}/data/task_list.json'
    
    with open(file_path, 'r', encoding='utf8') as file:
        task_list.extend(json.load(file))

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
