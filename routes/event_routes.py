from flask import Blueprint, request, jsonify
from flask_login import login_required
from models.event import Event
from extensions import db
from celery_tasks.tasks import send_reminder
from datetime import datetime

event_bp = Blueprint('event', __name__)


@event_bp.route('/events', methods=['POST'])
@login_required
def create_event():
    data = request.get_json()
    end_time = (datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S')
                if 'end_time' in data else None)
    reminder_time = (datetime.strptime(data['reminder_time'],
                                       '%Y-%m-%d %H:%M:%S')
                     if 'reminder_time' in data else None)

    new_event = Event(
        title=data['title'],
        description=data.get('description', ''),
        start_time=datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S'),
        end_time=end_time,
        reminder_time=reminder_time
    )
    db.session.add(new_event)
    db.session.commit()

    # Планируем задачу с Celery для напоминания
    if reminder_time:
        send_reminder.apply_async((new_event.id,), eta=reminder_time)

    return jsonify({'message': 'Event created successfully!'}), 201


# Маршрут для получения всех событий
@event_bp.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'start_time': event.start_time.strftime('%Y-%m-%d %H:%M:%S'),
        'end_time': (event.end_time.strftime('%Y-%m-%d %H:%M:%S')
                     if event.end_time else None)
    } for event in events])
