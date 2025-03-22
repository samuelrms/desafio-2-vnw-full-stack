import sqlite3
import os
from flask import g, current_app # type: ignore
from urllib.parse import urlparse

def get_db():
    if 'db' not in g:
        # Obter URL do banco de dados das variáveis de ambiente
        db_url = os.getenv('DATABASE_URL', 'sqlite:///database.db')
        parsed_url = urlparse(db_url)
        
        if parsed_url.scheme == 'sqlite':
            db_path = parsed_url.path[1:]  # Remove a barra inicial
            g.db = sqlite3.connect(db_path)
            g.db.row_factory = sqlite3.Row
        else:
            raise ValueError("Database scheme not supported")
    return g.db