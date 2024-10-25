# Calendar Reminder Application 📅

[![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)](https://www.python.org/downloads/release/python-390/)
[![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![Redis](https://img.shields.io/badge/Redis-7.0-red?logo=redis)](https://redis.io/)
[![Celery](https://img.shields.io/badge/Celery-5.4-green?logo=celery)](https://docs.celeryq.dev/)

## About The Project 🎯

Calendar Reminder - это веб-приложение, разработанное для управления событиями и автоматической отправки напоминаний. Проект демонстрирует работу с асинхронными задачами, управление базой данных и реализацию RESTful API.

### Ключевые функции:
- 👤 Аутентификация пользователей
- 📝 Создание и управление событиями
- ⏰ Автоматические email-напоминания
- 🔄 Асинхронная обработка задач

## Технический стек 🛠️

### Backend
- Python 3.9
- Flask (веб-фреймворк)
- SQLAlchemy (ORM)
- Flask-Login (аутентификация)
- Celery (асинхронные задачи)
- Redis (брокер сообщений)
- Docker (контейнеризация)

## Архитектура проекта 🏗️

```
calendar_reminder_project/
├── app.py                 # Основной файл приложения
├── extensions.py          # Инициализация расширений Flask
├── models/               
│   ├── user.py           # Модель пользователя
│   └── event.py          # Модель события
├── routes/
│   ├── auth.py           # Маршруты аутентификации
│   └── event_routes.py   # Маршруты для работы с событиями
├── celery_tasks/
│   └── tasks.py          # Асинхронные задачи Celery
├── docker-compose.yml    # Конфигурация Docker
└── requirements.txt      # Зависимости проекта
```

## API Endpoints 🌐

### Аутентификация
```http
POST /register          # Регистрация нового пользователя
POST /login            # Вход в систему
POST /logout           # Выход из системы
```

### События
```http
GET  /events           # Получение списка событий
POST /events           # Создание нового события
```

## Запуск проекта 🚀

1. Клонируйте репозиторий:
```bash
git clone git@github.com:svitlanasheptur/calendar_reminder_project.git
cd calendar_reminder_project
```

2. Запустите проект через Docker:
```bash
docker-compose up --build
```

Приложение будет доступно по адресу: http://localhost:5000

## Примеры использования 📝

### Создание события
```bash
curl -X POST http://localhost:5000/events \
-H "Content-Type: application/json" \
-d '{
    "title": "Важная встреча",
    "description": "Обсуждение проекта",
    "start_time": "2024-10-26 10:00:00",
    "reminder_time": "2024-10-26 09:45:00"
}'
```

## Планы по развитию 🎯

- [ ] Добавить веб-интерфейс
- [ ] Реализовать повторяющиеся события
- [ ] Добавить различные типы напоминаний (SMS, Push)
- [ ] Интеграция с календарями Google/Outlook

## Контакты 📫

[![Gmail](https://img.shields.io/badge/Gmail-red?logo=gmail&logoColor=white)](mailto:ssheptur@gmail.com)
[![Telegram](https://img.shields.io/badge/Telegram-blue?logo=telegram)](https://t.me/SvetaSheptur)

---
*Разработано Светланой Шептур © 2024*