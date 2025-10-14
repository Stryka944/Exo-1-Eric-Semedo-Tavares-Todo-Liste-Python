import json
import os
from models.task import Task

class TaskController:
    """
    Gère les tâches : ajout, suppression, lecture, et sauvegarde dans un fichier JSON.
    """

    def __init__(self, filepath="data/tasks.json"):
        self.filepath = filepath
        os.makedirs("data", exist_ok=True)
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Charge les tâches depuis le fichier JSON."""
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                try:
                    data = json.load(f)
                    return [Task(t["title"]) for t in data]
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self):
        """Sauvegarde les tâches dans le fichier JSON."""
        with open(self.filepath, "w") as f:
            json.dump([{"title": t.title} for t in self.tasks], f, indent=2)

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        self.save_tasks()
        return task

    def get_all_tasks(self):
        return self.tasks

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted = self.tasks.pop(index)
            self.save_tasks()
            return deleted
        return None
