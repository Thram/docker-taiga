from .celery import *
from kombu import Queue
import environ

print("Setup celery_local.py init")

env = environ.Env()

RABBITMQ_DEFAULT_USER = env('RABBITMQ_DEFAULT_USER', default='taiga')
RABBITMQ_DEFAULT_PASS = env('RABBITMQ_DEFAULT_PASS', default='taiga')
RABBITMQ_DEFAULT_VHOST = env('RABBITMQ_DEFAULT_VHOST', default='taiga')

broker_url = 'amqp://{}:{}@rabbitmq:5672/{}'.format(
    RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS, RABBITMQ_DEFAULT_VHOST)
result_backend = 'redis://redis:6379/0'

print("Setup celery_local.py finished")


# Values are 'pickle', 'json', 'msgpack' and 'yaml'
accept_content = ['pickle', ]
task_serializer = "pickle"
result_serializer = "pickle"

timezone = 'Pacific/Auckland'

task_default_queue = 'tasks'
task_queues = (
    Queue('tasks', routing_key='task.#'),
    Queue('transient', routing_key='transient.#', delivery_mode=1)
)
task_default_exchange = 'tasks'
task_default_exchange_type = 'topic'
task_default_routing_key = 'task.default'
