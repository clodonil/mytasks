import os

SECRET_KEY = "you-will-never-guess"
DEBUG = True

PORT = 8080
HOST = "0.0.0.0"

# MongoDB
#MONGODB_SETTINGS['host'] = 'mongodb://localhost/mytasks'
MONGODB_SETTINGS = {
    'host': 'mongodb://localhost/mytasks'
}
