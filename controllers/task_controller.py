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
    
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
        return None

    def get_all_tasks(self):
        return self.tasks
