from flask import Flask
from extensions import (
    db, login_manager, migrate, mail,
    init_celery
)
from routes.auth import auth_bp
from routes.event_routes import event_bp


def create_app():
    app = Flask(__name__)

    # Конфигурация
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Настройки Mail
    app.config['MAIL_SERVER'] = 'localhost'
    app.config['MAIL_PORT'] = 8025
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = False

    # Инициализация расширений
    mail.init_app(app)

    # Настройки Celery
    app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

    # Инициализация расширений
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    migrate.init_app(app, db)
    mail.init_app(app)
    init_celery(app)

    # Главная страница
    @app.route('/')
    def index():
        return "Welcome to the Calendar App!"

    # Регистрация blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(event_bp)

    return app


# Создание экземпляра приложения
app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
