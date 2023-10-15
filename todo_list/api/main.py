from flask import Blueprint, jsonify, request
from todo_list.db.models import Todo
from todo_list.db import db
from todo_list.serializers.serializers import Task, Tasks
from flask_pydantic_spec import Response, Request
from todo_list.serializers import spec


bp = Blueprint("todo", __name__)


@bp.route("/tasks", methods=["GET"])
@spec.validate(resp=Response(HTTP_200=Tasks))
def get_tasks():
    """Retorna todas as Tasks do banco de dados"""
    tasks = db.session.query(Todo).all()
    task_schema = [task.to_dict() for task in tasks]
    return jsonify(Tasks(tasks=task_schema, count=len(task_schema)).dict())


@bp.route("/tasks/<int:id>", methods=["GET"])
@spec.validate(resp=Response(HTTP_200=Task))
def get_task_with_id(id):
    """Retorna uma Task pelo ‘id’"""
    task = db.session.query(Todo).filter_by(id=id).first()
    if task is None:
        return {"message": "Task not found"}, 404
    return jsonify(task.to_dict())


@bp.route("/tasks/<title>", methods=["GET"])
@spec.validate(resp=Response(HTTP_200=Task))
def get_task_with_title(title):
    """Retorna uma Task pelo title"""
    tasks = db.session.query(Todo).filter_by(title=title).first()
    if tasks is None:
        return {"message": "Task not found"}, 404
    return jsonify(tasks.to_dict())


@bp.route("/tasks", methods=["POST"])
@spec.validate(body=Request(Task), resp=Response(HTTP_201=Task))
def add_task():
    """Insere uma Task no banco de dados"""
    body = request.context.body.dict()
    task = Todo(**body)
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


@bp.route("/tasks/<int:id>", methods=["PUT"])
@spec.validate(body=Request(Task), resp=Response(HTTP_201=Task))
def edit_task(id):
    """Altera as informações de uma Task especifica"""
    task = db.get_or_404(Todo, id)
    body = request.context.body.dict()
    task.title = body["title"]
    task.description = body["description"]
    task.done = body["done"]
    db.session.commit()

    return jsonify(Task(**body).dict())


@bp.route("/tasks/<int:id>", methods=["DELETE"])
@spec.validate(resp=Response("HTTP_200"))
def delete_task(id):
    """Deleta uma Task"""
    task = db.get_or_404(Todo, id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deletada com sucesso!"})
