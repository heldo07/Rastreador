from flask import Blueprint, render_template, request, redirect, url_for, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        # Exemplo fixo, adapte para seu usuário real
        if email == 'admin@painel.com' and senha == '1234':
            session['logado'] = True
            session['usuario_id'] = 1
            return redirect(url_for('dashboard.dashboard'))
        else:
            erro = "Credenciais inválidas"
    return render_template('login.html', erro=erro)

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
