from flask import Blueprint, render_template, redirect, session, url_for

admin_bp = Blueprint('admin', __name__,template_folder='../templates')

@admin_bp.route('/dashboard')
def dashboard():
    if not session.get('logado'):
        return redirect(url_for('login'))  # Corrigido aqui
    return render_template('dashboard.html')

# 🔹 Rota de logout
@admin_bp.route('/logout')
def logout():
    session.clear()  # Remove todos os dados da sessão
    return redirect(url_for('login'))  # Redireciona para a tela de login