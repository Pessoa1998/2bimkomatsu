from app import app, db  # Certifique-se de que 'app' e 'db' estão importados corretamente

with app.app_context():
    db.create_all()
