#!/bin/sh
set -e

echo "⏳ Aguardando o banco de dados em $POSTGRES_HOST:$POSTGRES_PORT..."

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 2
done

echo "✅ Banco pronto! Executando comando..."
exec "$@"