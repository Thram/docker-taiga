#!/bin/sh
set -e

if [ ! -f /taiga_events/config.json ]; then
    echo "Generating /taiga_events/config.json file..."
    cat > /taiga_events/config.json <<EOF
{
    "url": "amqp://$RABBITMQ_USER:$RABBITMQ_PASSWORD@${RABBITMQ_HOST:-rabbitmq}:${RABBITMQ_PORT:-5672}/$RABBITMQ_VHOST",
    "secret": "$DJANGO_SECRET_KEY",
    "webSocketServer": {
        "port": 8888
    }
}

EOF
fi

exec "$@"
