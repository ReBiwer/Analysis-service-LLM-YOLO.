# Analysis Service

Сервис для анализа изображений с использованием YOLO (детекция объектов) и LLM (анализ содержимого).

## Описание задачи

Сервис принимает изображение в формате base64 и текстовый запрос пользователя, затем:

1. **Детекция объектов**: Использует модель YOLO11n для определения объектов на изображении
2. **LLM анализ**: Обрабатывает запрос пользователя и результаты детекции через OpenAI API
3. **Логирование**: Сохраняет все запросы и ответы в базе данных PostgreSQL

## Стек технологий

### Backend
- **Python 3.12+** - основной язык
- **FastAPI** - веб-фреймворк для создания REST API
- **Ultralytics YOLO** - модель компьютерного зрения для детекции объектов
- **LangChain + OpenAI** - фреймворк для работы с LLM
- **Dishka** - система dependency injection

### База данных
- **PostgreSQL** - основная база данных
- **SQLAlchemy** - ORM для работы с базой данных  
- **Alembic** - система миграций базы данных

### Развертывание
- **Docker + Docker Compose** - контейнеризация и оркестрация
- **uvicorn** - ASGI сервер

## API Endpoints

### POST `/yolo/analyze`
Анализ изображения

**Пример запроса:**
```json
{
  "query": "Сколько машин на картинке и какие из них опасные?",
  "image_64": "base64_encoded_image_string"
}
```

> **💡 Для тестирования:** В проекте есть готовые тестовые файлы:
> - `test_img.png` - тестовое изображение
> - `test_img.base_64.txt` - то же изображение в формате base64 (готово для вставки в `image_64`)

**Пример ответа:**
```json
{
  "detected_objects": [
    "traffic light ID:9",
    "car ID:2",
    "traffic light ID:9",
    "traffic light ID:9",
    "stop sign ID:11",
    "person ID:0",
    "person ID:0",
    "person ID:0",
    "stop sign ID:11",
    "person ID:0",
    "car ID:2",
    "truck ID:7",
    "sports ball ID:32",
    "fire hydrant ID:10"
  ],
  "llm_response": "На фото изображены светофоры, автомобили, люди, знаки стоп и пожарный гидрант. Это может быть опасно, если люди не соблюдают правила дорожного движения или если автомобили движутся слишком быстро."
}
```

### GET `/yolo/logs`
Получение логов анализа

**Параметры:**
- `count_record` (опционально) - количество записей (по умолчанию 10)

## Настройка и запуск

### 1. Клонирование репозитория
```bash
git clone <your-repo-url>
cd analysis_service
```

### 2. Настройка переменных окружения
Скопируйте файл `.env.example` в `.env` и заполните необходимые значения:

```bash
cp .env.example .env
```

Отредактируйте файл `.env` согласно инструкциям в шаблоне.

### 2.1. Настройка Shadowsocks прокси (опционально)
Проект поддерживает использование Shadowsocks прокси для доступа к внешним API (например, OpenAI). 

Если вы хотите использовать Shadowsocks прокси:
1. Следуйте инструкции по настройке: [Инструкция по настройке Shadowsocks](https://losst.pro/nastrojka-shadowsocks)
2. Укажите URL прокси в переменной `PROXY_URL` в файле `.env`

### 3. Запуск через Docker Compose
```bash
# Запуск всех сервисов
docker-compose up -d

# Просмотр логов
docker-compose logs -f

# Остановка сервисов
docker-compose down
```

### 4. Применение миграций
Миграции применяются автоматически при запуске контейнера backend.

## Разработка

### Локальная разработка
Для локальной разработки рекомендуется использовать **uv** для управления зависимостями:

```bash
# Установка зависимостей
uv sync

# Активация виртуального окружения
source .venv/bin/activate

# Запуск в режиме разработки
cd app
python main.py
```

### Структура проекта
```
analysis_service/
├── app/
│   ├── api/              # API endpoints
│   ├── db/               # Конфигурация БД и DAO
│   ├── di/               # Dependency injection
│   ├── migrations/       # Миграции Alembic
│   ├── models/          # SQLAlchemy модели
│   ├── schemas/         # Pydantic схемы
│   ├── services/        # Бизнес-логика (YOLO, LLM)
│   ├── use_cases/       # Use cases (сценарии использования)
│   ├── config.py        # Конфигурация приложения
│   └── main.py          # Точка входа
├── docker-compose.yaml  # Конфигурация Docker Compose
├── pyproject.toml       # Зависимости Python
└── env.example          # Шаблон переменных окружения
```

## Доступ к сервису

После запуска сервис будет доступен по адресу:
- **API**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

База данных PostgreSQL:
- **Хост**: localhost:5432
- **База данных**: значение из переменной `DB_NAME`