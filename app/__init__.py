from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Inicializa instâncias globais
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configurações
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_dir, 'database.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'chave_super_secreta'

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Importa e registra rotas
    from app.controllers.nutricionista_routes import bp as nutricionista_bp
    app.register_blueprint(nutricionista_bp)

    return app
