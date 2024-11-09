# from app import app, db  # Verifique se o caminho está correto para o arquivo 'app'

# # Inicializa o banco de dados com o contexto do aplicativo
# with app.app_context():
#     db.create_all()

# # Verifica se a aplicação está sendo executada no ambiente correto
# if __name__ == "__main__":
#     app.run()





from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicialize o app e o banco de dados
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'  # Exemplo de URI, ajuste conforme seu banco de dados
db = SQLAlchemy(app)

# Se precisar criar tabelas
with app.app_context():
    db.create_all()

# Exemplo de rota simples para testar
@app.route("/")
def home():
    return "Aplicação Flask está rodando!"

# Código para rodar localmente (não afeta o deploy no Vercel)
if __name__ == "__main__":
    app.run()
