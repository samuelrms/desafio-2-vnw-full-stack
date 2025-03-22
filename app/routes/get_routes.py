from flask import Blueprint, jsonify # type: ignore
from app.config.database import get_db

get_routes = Blueprint('get_routes', __name__)

@get_routes.route('/')
def home():
    return "📚 Bem-vindo à Livraria Vai Na Web - Doe conhecimento!"

@get_routes.route('/livros')
def listar_livros():
    db = get_db()
    livros = db.execute('SELECT * FROM LIVROS').fetchall()
    return jsonify([dict(livro) for livro in livros])