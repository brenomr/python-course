"""
Create a task list, allowing the user to
add, undo and redo items to the list.

Commands:
(List, Undo, Redo, Clear and Exit)
"""

import os

def clear():
    os.system("clear")

def print_tasks(task_list: list):
    print("TASKS:\n------")
    print(*task_list, sep="\n", end="\n"*2)

def add_task(task: str, task_list: list):
    task_list.append(task)

def undo_task(task_list: list, cache_list: list):
    if len(task_list) > 0:
        task_removed = task_list.pop()
        cache_list.append(task_removed)

welcome_message = "Welcome to Task List V0.0.1!\n\nType one of the commands or start\ntyping your task to create a list\n"

def task():

    continue_adding = True
    options = ['list', 'undo', 'redo', 'exit', 'clear']
    task_list = []
    cache_list = []

    print(welcome_message)
    
    while continue_adding:
        print("-"*47)
        print("Commands: | list | undo | redo | exit | clear |")
        print("-"*47, end='\n'*2)

        input_task = input('Command or Task: ').lower()

        if input_task not in options:
            add_task(input_task, task_list)
            if len(cache_list) > 0:
                cache_list = []
            clear()
            print('\nTask created!\n')
        
        if input_task == options[0]:
            clear()
            print_tasks(task_list)
        
        if input_task == options[1]:
            undo_task(task_list, cache_list)

        if input_task == options[2]:
            undo_task(cache_list, task_list)
        
        if input_task == options[3]:
            clear()
            continue_adding = False

        if input_task == options[4]:
            clear()

task()
