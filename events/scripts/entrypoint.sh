#!/bin/sh
set -e
if [ ! -f /taiga_events/config.json ]; then
    echo "Generating /taiga_events/config.json file..."
    RABBITMQ_USER = ${RABBITMQ_USER:-"taiga"}
    RABBITMQ_PASSWORD = ${RABBITMQ_PASSWORD:-"taiga"}
    RABBITMQ_VHOST = ${RABBITMQ_VHOST:-"taiga"}
    cat > /taiga_events/config.json <<EOF
{
    "url": "amqp://$RABBITMQ_USER:$RABBITMQ_PASSWORD@rabbitmq:5672/$RABBITMQ_VHOST",
    "secret": "$DJANGO_SECRET_KEY",
    "webSocketServer": { "port": 8888 }
}

EOF
fi

exec "$@"
