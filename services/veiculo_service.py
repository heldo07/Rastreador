'''from models import db, Veiculo

def salvar_veiculo(dados):
    veiculo = Veiculo(
        placa=dados['placa'],
        modelo=dados['modelo'],
        ano=dados['ano']
    )
    db.session.add(veiculo)
    db.session.commit()
    return veiculo
'''