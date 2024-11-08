# #comentando código do routes e logo abaixo haverá uma nova estrutura para uso

# # app/routes.py
# from app import app, db
# from app.models import Item
# from flask import render_template, request, redirect, url_for

# @app.route('/')
# @app.route('/cadastro', methods=['GET', 'POST'])
# def cadastro():
#     if request.method == 'POST':
#         nome = request.form['nome']
#         descricao = request.form['descricao']
#         preco = request.form['preco']
#         quantidade = request.form['quantidade']
        
#         # Criação de um novo item no banco de dados
#         novo_item = Item(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
#         db.session.add(novo_item)
#         db.session.commit()
        
#         # Redireciona para a página de visualização após cadastro
#         return redirect(url_for('visualizar'))
    
#     return render_template('cadastro.html')

# @app.route('/visualizar')
# def visualizar():
#     # Consulta os itens cadastrados no banco de dados
#     itens = Item.query.all()
#     return render_template('visualizar.html', itens=itens)


# @app.route('/editar/<int:id>')
# def editar(id):
#     # Lógica para editar o item com o ID fornecido
#     pass

# @app.route('/excluir/<int:id>', methods=['POST'])
# def excluir(id):
#     # lógica para excluir o item com o ID fornecido
#     pass





































# app/routes.py
from app import app, db
from app.models import Item
from flask import render_template, request, redirect, url_for, jsonify

@app.route('/')
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        quantidade = request.form['quantidade']
        
        # Criação de um novo item no banco de dados
        novo_item = Item(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
        db.session.add(novo_item)
        db.session.commit()
        
        # Redireciona para a página de visualização após cadastro
        return redirect(url_for('visualizar'))
    
    return render_template('cadastro.html')

@app.route('/visualizar')
def visualizar():
    # Consulta os itens cadastrados no banco de dados
    itens = Item.query.all()
    return render_template('visualizar.html', itens=itens)

@app.route('/excluir/<int:id>', methods=['DELETE'])
def excluir(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item excluído com sucesso'}), 200

@app.route('/editar/<int:id>', methods=['PUT'])
def editar(id):
    data = request.get_json()
    item = Item.query.get_or_404(id)
    
    item.nome = data.get('nome', item.nome)
    item.descricao = data.get('descricao', item.descricao)
    item.preco = data.get('preco', item.preco)
    item.quantidade = data.get('quantidade', item.quantidade)
    
    db.session.commit()
    return jsonify({'message': 'Item atualizado com sucesso'}), 200
