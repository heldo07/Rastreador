'''# routes/veiculo_routes.py

from flask import Blueprint, jsonify

veiculo_bp = Blueprint('veiculo', __name__)

@veiculo_bp.route('/api/veiculos', methods=['GET'])
def listar_veiculos():
    return jsonify({"mensagem": "Listando veículos"})
'''