from models.task import Task

class TaskController:
    """
    Gère la logique : ajouter et lister les tâches.
    """

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        return task

    def get_all_tasks(self):
        return self.tasks
