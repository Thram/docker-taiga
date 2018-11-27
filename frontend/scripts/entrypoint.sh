#!/bin/sh

set -o errexit
set -o pipefail

if [ ! -f /taiga_frontend/conf.json ]; then
    echo "Generating /taiga_frontend/conf.json file..."
    API_URL=${API_URL:-\"/api/v1/\"}
    DEFAULT_LANGUAGE=${DEFAULT_LANGUAGE:-\"en\"}
    EVENTS_URL=${EVENTS_URL:-null}
    cat > /taiga_frontend/conf.json <<EOF
{
    "api": $API_URL,
    "eventsUrl": $EVENTS_URL,
    "eventsMaxMissedHeartbeats": 5,
    "eventsHeartbeatIntervalTime": 60000,
    "debug": ${DEBUG:-false},
    "debugInfo": ${DEBUG:-false},
    "defaultLanguage": $DEFAULT_LANGUAGE,
    "themes": ["taiga"],
    "defaultTheme": "taiga",
    "importers": ["trello"],
    "publicRegisterEnabled": ${PUBLIC_REGISTER_ENABLED:-true},
    "feedbackEnabled": true,
    "privacyPolicyUrl": null,
    "termsOfServiceUrl": null,
    "maxUploadFileSize": null,
    "contribPlugins": []
}
EOF
fi

exec "$@"
