# ~api/app/resources/routes.py

from .task import TasksApi, TaskApi
from .auth import SignupApi, LoginApi


def initialize_routes(api):
    api.add_resource(TasksApi, '/api/tasks')
    api.add_resource(TaskApi, '/api/tasks/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
