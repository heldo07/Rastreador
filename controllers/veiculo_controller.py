'''from flask import jsonify
from services.veiculo_service import salvar_veiculo

def criar_veiculo(dados):
    try:
        veiculo = salvar_veiculo(dados)
        return jsonify({'mensagem': 'Veículo cadastrado com sucesso', 'veiculo_id': veiculo.id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
'''