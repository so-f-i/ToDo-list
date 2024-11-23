from TodoList import TodoList
"""
The TodoList module contains the TodoList class, which manages the task list, allowing you to add, delete, view and change the status of tasks. 
Tasks are saved and downloaded from a file in JSON format.
"""
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
