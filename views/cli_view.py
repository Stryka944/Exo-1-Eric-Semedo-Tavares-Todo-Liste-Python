class CLIView:
    """
    Vue console : gère les affichages et saisies utilisateur.
    """

    @staticmethod
    def show_menu():
        print("\n=== ToDoList CLI ===")
        print("1. Ajouter une tâche")
        print("2. Voir toutes les tâches")
        print("3. Supprimer une tâche")
        print("4. Quitter")

    @staticmethod
    def ask_user_input(prompt):
        return input(prompt)

    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("\nAucune tâche enregistrée.")
        else:
            print("\nVos tâches :")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
