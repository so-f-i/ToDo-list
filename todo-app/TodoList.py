import json
import os

from Task import Task
"""
The Task module contains the Task class, which is a task with a description and status of completion. 
The class includes functions for changing the status of a task, converting a task to a dictionary, and creating a task from a dictionary.
"""
class TodoList:
    def __init__(self, filename='tasks.json'):
        # Initializing the task list and downloading from a file
        """:param filename: The name of the file to save and load tasks"""
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, description):
        # Adding a new task to the list
        """:param description: Description of the task to be added"""
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        # Deleting a task by index
        """:param index: Index of the task to be deleted"""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
        else:
            print("🚫 Индекс вне диапазона!")

    def view_tasks(self):
        """:return:View all tasks as a table."""
        if not self.tasks:
            print("📋 Список задач пуст!")
            return

        print(f"\n{'№':<5}{'Описание задачи':<30}{'Статус':<10}")
        print("-" * 50)
        for index, task in enumerate(self.tasks):
            status = "✅" if task.completed else "❌"
            print(f"{index + 1:<5}{task.description:<30}{status:<10}")

    def mark_task_completed(self, index):
        """
        Marking a task as completed
        :param index: Index of the task to be completed
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()

    def save_tasks(self):
        """Saving tasks to a file in JSON format"""
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def load_tasks(self):
        """Downloading tasks from a file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(task) for task in tasks_data]