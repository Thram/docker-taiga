from .celery import *
import environ

print("Setup init")

env = environ.Env()

# CELERY_IMPORTS = ('taiga.importers.trello.tasks.import_project' )
RABBITMQ_DEFAULT_USER = env('RABBITMQ_DEFAULT_USER', default='taiga')
RABBITMQ_DEFAULT_PASS = env('RABBITMQ_DEFAULT_PASS', default='taiga')
RABBITMQ_DEFAULT_VHOST = env('RABBITMQ_DEFAULT_VHOST', default='taiga')

broker_url = 'amqp://{}:{}@rabbitmq:5672/{}'.format(
    RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS, RABBITMQ_DEFAULT_VHOST)
result_backend = 'redis://redis:6379/0'

print("Setup finished")
