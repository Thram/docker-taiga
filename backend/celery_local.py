from .celery import *
import environ

env = environ.Env()

CONFIG = {
    'RABBITMQ_USER': env('RABBITMQ_USER',  default='taiga'),
    'RABBITMQ_PASSWORD': env('RABBITMQ_PASSWORD',  default='taiga'),
    'RABBITMQ_VHOST': env('RABBITMQ_VHOST',  default='taiga'),
    'RABBITMQ_HOST': env('RABBITMQ_HOST',  default='rabbitmq'),
    'RABBITMQ_PORT': env('RABBITMQ_PORT',  default='5672'),
    'REDIS_HOST': env('REDIS_HOST',  default='redis'),
    'REDIS_PORT': env('REDIS_PORT',  default='6379'),
}

RABBITMQ_USER = CONFIG['RABBITMQ_USER']
RABBITMQ_PASSWORD = CONFIG['RABBITMQ_PASSWORD']
RABBITMQ_VHOST = CONFIG['RABBITMQ_VHOST']
RABBITMQ_HOST = CONFIG['RABBITMQ_HOST']
RABBITMQ_PORT = CONFIG['RABBITMQ_PORT']
REDIS_HOST = CONFIG['REDIS_HOST']
REDIS_PORT = CONFIG['REDIS_PORT']

broker_url = "amqp://{}:{}@{}:{}/{}".format(
    RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_VHOST)
result_backend = "redis://{}:{}/0".format(REDIS_HOST, REDIS_PORT)
