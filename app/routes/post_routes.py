from flask import Blueprint, request, jsonify # type: ignore
from app.config.database import get_db

post_routes = Blueprint('post_routes', __name__)

@post_routes.route('/doar', methods=['POST'])
def doar_livro():
    data = request.get_json()
    campos_obrigatorios = ['titulo', 'categoria', 'autor', 'imagem_url']
    
    if not all(campo in data for campo in campos_obrigatorios):
        return jsonify({"erro": "Campos obrigatórios faltando!"}), 400
    
    db = get_db()
    try:
        cursor = db.execute('''
            INSERT INTO LIVROS (titulo, categoria, autor, imagem_url)
            VALUES (?, ?, ?, ?)
        ''', (data['titulo'], data['categoria'], data['autor'], data['imagem_url']))
        db.commit()
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
    novo_livro = db.execute('SELECT * FROM LIVROS WHERE id = ?', (cursor.lastrowid,)).fetchone()
    return jsonify(dict(novo_livro)), 201