from app import create_app, db
from app.models import nutricionista

app = create_app()

# Cria o banco automaticamente caso não exista
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
