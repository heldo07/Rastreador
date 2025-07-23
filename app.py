
from flask import Flask, request, jsonify, render_template, redirect, url_for,session
from config import Config
from models import db, Veiculo, Localizacao
from datetime import datetime
import psycopg2

def create_app():
    app = Flask(__name__)
    app.secret_key = '071507'
    app.config.from_object(Config)
    db.init_app(app)

    # Registrar blueprint administrativo
    


    # 🔹 Rota raiz
    @app.route('/')
    def home():
        return redirect(url_for('login'))

    # 🔹 Rota de login
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        erro = None
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            if email == 'admin@painel.com' and senha == '1234':
                return "<h2>✅ Login bem-sucedido!</h2>"
            else:
                erro = "Credenciais inválidas"
        return render_template('login.html', erro=erro)

    # 🔹 Cadastrar veículo
    @app.route('/veiculos', methods=['POST'])
    def criar_veiculo():
        data = request.get_json()
        novo = Veiculo(
            placa=data['placa'],
            modelo=data['modelo']
        )
        db.session.add(novo)
        db.session.commit()
        return jsonify({'mensagem': 'Veículo cadastrado com sucesso'}), 201

    # 🔹 Listar veículos
    @app.route('/veiculos', methods=['GET'])
    def listar_veiculos():
        veiculos = Veiculo.query.all()
        return jsonify([{
            'id': v.id,
            'placa': v.placa,
            'modelo': v.modelo,
            'ativo': v.ativo
        } for v in veiculos])

    # 🔹 Atualizar localização
    @app.route('/localizacao', methods=['POST'])
    def registrar_localizacao():
        data = request.get_json()
        nova = Localizacao(
            veiculo_id=data['veiculo_id'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            timestamp=datetime.utcnow()
        )
        db.session.add(nova)
        db.session.commit()
        return jsonify({'mensagem': 'Localização registrada com sucesso'}), 201

    # 🔹 Última localização
    @app.route('/veiculos/<int:veiculo_id>/localizacao', methods=['GET'])
    def ultima_localizacao(veiculo_id):
        loc = Localizacao.query.filter_by(veiculo_id=veiculo_id).order_by(Localizacao.timestamp.desc()).first()
        if loc:
            return jsonify({
                'latitude': loc.latitude,
                'longitude': loc.longitude,
                'timestamp': loc.timestamp
            })
        return jsonify({'mensagem': 'Nenhuma localização encontrada'}), 404

    return app


# ✅ Rodar o app
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        print("✅ Banco de dados conectado e tabelas criadas.")
    app.run(debug=True)

    
# Rota inicial
@app.route('/')
def index():
    return redirect(url_for('login'))

try:
    conn = psycopg2.connect(
        host="localhost",
        database="rastreador_db",
        user="postgres",
        password="0715"
    )
    print("Conexão OK!")
    conn.close()
except Exception as e:
    print("Erro:", e)

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if email == 'admin@painel.com' and senha == '1234':
            session['logado'] = True  # 🔒 Marca que está logado
            return redirect(url_for('admin.dashboard'))  # Vai pro painel
        else:
            erro = "Credenciais inválidas"
    return render_template('login.html', erro=erro)

if __name__ == '__main__':
    app.run(debug=True)


'''from flask import Flask
from config import Config
from database import db  # ← importando do database/__init__.py

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Aqui você registra as rotas (blueprints)
    from routes.veiculo_routes import veiculo_bp
    app.register_blueprint(veiculo_bp)

    return app

# Rodar direto com python app.py
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
        print("✅ Banco de dados conectado e tabelas criadas.")
    app.run(debug=True)'''