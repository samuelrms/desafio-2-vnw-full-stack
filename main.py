from flask import Flask # type: ignore
from app.config.database import init_db, close_db
from app.routes.get_routes import get_routes
from app.routes.post_routes import post_routes

app = Flask(__name__)
app.config['DATABASE'] = 'database.db'

with app.app_context():
    init_db()

app.register_blueprint(get_routes)
app.register_blueprint(post_routes)

app.teardown_appcontext(close_db)

if __name__ == '__main__':
    app.run(debug=True)