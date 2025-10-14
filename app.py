from flask import Flask, jsonify, request
from controllers.task_controller import TaskController

app = Flask(__name__)
controller = TaskController()

@app.route("/")
def home():
    return jsonify({"message": "Bienvenue sur la ToDoList Flask API"}), 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = controller.get_all_tasks()
    return jsonify([{"id": i, "title": t.title} for i, t in enumerate(tasks)])

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Titre manquant"}), 400
    task = controller.add_task(data["title"])
    return jsonify({"message": f"Tâche '{task.title}' ajoutée"}), 201

@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    deleted = controller.delete_task(index)
    if deleted:
        return jsonify({"message": f"Tâche supprimée : {deleted.title}"}), 200
    return jsonify({"error": "Numéro invalide"}), 404

if __name__ == "__main__":
    app.run(debug=True)
