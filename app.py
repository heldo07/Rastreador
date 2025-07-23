
# app.py
from flask import Flask
from config import Config
from models import db
from routes.veiculo_routes import veiculo_bp
from routes.auth_routes import auth_bp
from routes.dashboard import dashboard_bp
import psycopg2

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = '071507'

    db.init_app(app)

    # Registrando blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(veiculo_bp)
    app.register_blueprint(dashboard_bp)

    return app

# Testando conexão com o banco
try:
    conn = psycopg2.connect(
        host="localhost",
        database="rastreador_db",
        user="postgres",
        password="0715"
    )
    print("✅ Conexão com o banco de dados estabelecida!")
    conn.close()
except Exception as e:
    print("❌ Erro ao conectar no banco:", e)
    exit(1)

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)



