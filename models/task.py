class Task:
    """
    Représente une tâche simple.
    """
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"- {self.title}"
