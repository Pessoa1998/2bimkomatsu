from app import app, db  # Verifique se o caminho está correto para o arquivo 'app'

# Inicializa o banco de dados com o contexto do aplicativo
with app.app_context():
    db.create_all()

# Verifica se a aplicação está sendo executada no ambiente correto
if __name__ == "__main__":
    app.run()
