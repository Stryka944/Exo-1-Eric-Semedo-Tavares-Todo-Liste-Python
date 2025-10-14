from controllers.task_controller import TaskController
from views.cli_view import CLIView

def main():
    controller = TaskController()
    view = CLIView()

    while True:
        view.show_menu()
        choice = view.ask_user_input("Choisissez une option : ")

        if choice == "1":
            title = view.ask_user_input("Entrez le titre de la tâche : ")
            if title.strip():
                controller.add_task(title)
                print(f"Tâche '{title}' ajoutée")
            else:
                print("⚠️ Le titre ne peut pas être vide.")
        elif choice == "2":
            tasks = controller.get_all_tasks()
            view.show_tasks(tasks)
        elif choice == "3":
            print("Au revoir")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()
