from app import db
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash


class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    dt_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    historico = db.Column(db.Text, nullable=True)
    id_nutricionista = db.Column(db.Integer, db.ForeignKey("nutricionistas.id"), nullable=False)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def idade(self):
        return date.today().year - self.dt_nascimento.year

    def __repr__(self):
        return f"<Cliente {self.nome}>"
