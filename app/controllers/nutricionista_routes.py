from flask import Blueprint, request, jsonify
from app import db
from app.models.nutricionista import Nutricionista

bp = Blueprint('nutricionista', __name__, url_prefix='/nutricionistas')

# Criar um nutricionista
@bp.route('/', methods=['POST'])
def criar_nutricionista():
    data = request.get_json(force=True)

    campos = {
        "nome": data.get("nome"),
        "email": data.get("email"),
        "senha_hash": data.get("senha_hash"),
        "registro_profissional": data.get("registro_profissional"),
        "metodologia_json": data.get("metodologia_json"),
    }

    novo = Nutricionista(**campos)  # desempacota o dicionário
    db.session.add(novo)
    db.session.commit()

    return jsonify(novo.to_dict()), 201

# Listar todos
@bp.route('/', methods=['GET'])
def listar_nutricionistas():
    nutricionistas = Nutricionista.query.all()
    return jsonify([n.to_dict() for n in nutricionistas])

# Buscar por ID
@bp.route('/<int:id>', methods=['GET'])
def buscar_nutricionista(id):
    nutricionista = Nutricionista.query.get_or_404(id)
    return jsonify(nutricionista.to_dict())

# Deletar
@bp.route('/<int:id>', methods=['DELETE'])
def deletar_nutricionista(id):
    nutricionista = Nutricionista.query.get_or_404(id)
    db.session.delete(nutricionista)
    db.session.commit()
    return jsonify({"mensagem": "Nutricionista removido com sucesso"})
