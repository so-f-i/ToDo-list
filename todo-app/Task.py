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