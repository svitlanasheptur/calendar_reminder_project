from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
from celery import Celery

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
mail = Mail()
celery = Celery()


def init_celery(app):
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    return User.query.get(int(user_id))
