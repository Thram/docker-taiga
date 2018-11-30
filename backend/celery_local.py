from .celery import *
import environ
import gevent.monkey

gevent.monkey.patch_all()

print("Setup celery_local.py init")

env = environ.Env()

RABBITMQ_USER = env('RABBITMQ_USER', default='taiga')
RABBITMQ_PASSWORD = env('RABBITMQ_PASSWORD', default='taiga')
RABBITMQ_VHOST = env('RABBITMQ_VHOST', default='taiga')

broker_url = 'amqp://{}:{}@rabbitmq:5672/{}'.format(
    RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_VHOST)
result_backend = 'redis://redis:6379/0'
timezone = 'Pacific/Auckland'

print("Setup celery_local.py finished")
