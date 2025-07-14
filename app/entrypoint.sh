#!/bin/bash
set -e

echo "🔄 Запускаем миграции..."
cd app
alembic upgrade head

echo "🚀 Запускаем сервер API..."
python main.py
