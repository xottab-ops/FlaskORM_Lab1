from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///structure.db"

    db.init_app(app)

    with app.app_context():
        from app.models import Country, City, Building, TypeBuilding
        db.create_all()

    from app.views import main_bp
    app.register_blueprint(main_bp)

    return app