from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from models import Veiculo,db 

veiculo_bp = Blueprint('veiculos', __name__)

@veiculo_bp.route('/veiculos', methods=['GET'])
def listar_veiculos():
    if not session.get('logado'):
        return redirect(url_for('auth.login'))
    veiculos = Veiculo.query.all()
    return render_template('veiculos.html', veiculos=veiculos)

@veiculo_bp.route('/veiculos', methods=['POST'])
def criar_veiculo():
    data = request.get_json()
    novo = Veiculo(
        placa=data['placa'],
        modelo=data['modelo']
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify({'mensagem': 'Veículo cadastrado com sucesso'}), 201

    

@veiculo_bp.route('/veiculos/<int:id>/editar', methods=['GET', 'POST'])
def editar_veiculo(id):
    if not session.get('logado'):
        return redirect(url_for('auth.login'))
    veiculo = Veiculo.query.get_or_404(id)
    if request.method == 'POST':
        veiculo.placa = request.form['placa']
        veiculo.modelo = request.form['modelo']
        ativo_str = request.form.get('ativo')
        veiculo.ativo = True if ativo_str == 'on' else False
        db.session.commit()
        return redirect(url_for('veiculos.listar_veiculos'))
    return render_template('editar_veiculo.html', veiculo=veiculo)

@veiculo_bp.route('/veiculos/<int:id>/excluir', methods=['POST'])
def excluir_veiculo(id):
    if not session.get('logado'):
        return redirect(url_for('auth.login'))
    veiculo = Veiculo.query.get_or_404(id)
    db.session.delete(veiculo)
    db.session.commit()
    return redirect(url_for('veiculos.listar_veiculos'))
