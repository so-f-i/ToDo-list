import json
import os

class Task:
    def __init__(self, description, completed=False):
        # Initializing a task with a description and execution status
        """
        :param description: Description of the task.
        :param completed: Task completion status (False by default).
        """
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        # Converting a task to a dictionary for saving in JSON
        """:return: Dictionary with fields 'description' and 'completed'"""
        return {'description': self.description, 'completed': self.completed}

    @classmethod
    def from_dict(cls, data):
        # Creating an instance of a task from a dictionary
        """
        :param data: A dictionary with task data.
        :return: An instance of the Task class.
        """
        return cls(data['description'], data['completed'])


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
        # Marking a task as completed
        """:param index: Index of the task to be completed"""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()

    def save_tasks(self):
        # Saving tasks to a file in JSON format
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def load_tasks(self):
        # Downloading tasks from a file
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(task) for task in tasks_data]

def main():
    todo_list = TodoList()  # Creating an instance of the ToDo list
    while True:

        print("\n🔧 Действия: 1 - Добавить, 2 - Удалить, 3 - Просмотреть, 4 - Завершить, 5 - Выход")
        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            task_desc = input("Введите описание задачи: ")
            todo_list.add_task(task_desc)
        elif choice == '2':
            todo_list.view_tasks()
            index = int(input("Введите номер задачи для удаления: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            todo_list.view_tasks()
            index = int(input("Введите номер задачи для завершения: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == '5':
            print("👋 Выход из программы.")
            break
        else:
            print("🚫 Пожалуйста, выберите корректное действие.")

if __name__ == "__main__":
    main()