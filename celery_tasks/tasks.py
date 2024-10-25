from celery import Celery
from flask_mail import Mail, Message
from models.event import Event

# Настройки Celery с Redis
celery = Celery('tasks', broker='redis://redis:6379/0')

# Создание экземпляра Mail
mail = Mail()


def init_mail(app):
    mail.init_app(app)


@celery.task
def send_reminder(event_id):
    from flask import current_app

    event = Event.query.get(event_id)
    if event:
        with current_app.app_context():
            msg = Message(
                subject=f"Напоминание о событии: {event.title}",
                sender='no-reply@calendarapp.com',
                recipients=['ssheptur@gmail.com']
            )
            msg.body = (
                f"Не забудьте о событии '{event.title}', "
                f"которое начнется {event.start_time}."
            )
            mail.send(msg)
