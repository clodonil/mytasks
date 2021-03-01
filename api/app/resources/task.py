# ~api/app/resources/task.py


from flask_restful import Resource
from flask import Response, request
from app.database.models import Task, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime


class TasksApi(Resource):
    @jwt_required
    def get(self):
        tasks = Task.objects().to_json()
        return Response(tasks, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()

        date_task = datetime.strptime(body.get('date_task'), '%d/%m/%Y')
        body['date_task'] = date_task
        user = User.objects.get(id=user_id)
        task = Task(**body, added_by=user)
        task.save()
        user.update(push__tasks=task)
        user.save()
        id = task.id
        return {'id': str(id)}, 200


class TaskApi(Resource):
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        task = Task.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        if body.get('date_task') != None:
            date_task = datetime.strptime(body.get('date_task'), '%d/%m/%Y')
            body['date_task'] = date_task
        body['date_modified'] = datetime.now()
        Task.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        task = Task.objects.get(id=id, added_by=user_id)
        task.delete()
        return '', 200

    @jwt_required
    def get(self, id):
        tasks = Task.objects.get(id=id).to_json()
        return Response(tasks, mimetype="application/json", status=200)
