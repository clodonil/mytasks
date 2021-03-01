# ~api/app/database/models.py
from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
import datetime


class Task(db.Document):
    name = db.StringField(required=True, unique=True)
    date_created = db.DateTimeField(default=datetime.datetime.now())
    date_modified = db.DateTimeField(default=datetime.datetime.now())
    date_task = db.DateTimeField(required=True)
    status = db.StringField(default='criado')
    tags = db.ListField(db.StringField(max_length=30))
    added_by = db.ReferenceField('User')


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    tasks = db.ListField(db.ReferenceField(
        'Task', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


User.register_delete_rule(Task, 'added_by', db.CASCADE)
