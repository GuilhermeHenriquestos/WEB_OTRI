from app import db
from datetime import datetime

class Nutricionista(db.Model):
    __tablename__ = 'nutricionistas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(256), nullable=False)
    registro_profissional = db.Column(db.String(50), nullable=True)
    metodologia_json = db.Column(db.Text, nullable=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Nutricionista {self.nome}>"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "registro_profissional": self.registro_profissional,
            "metodologia_json": self.metodologia_json,
            "data_criacao": self.data_criacao.isoformat(),
        }
