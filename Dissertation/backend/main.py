from flask import Flask
from bson import json_util
import json
from flask_cors import CORS
from views.main2 import main_bp
from views.authentication import authentication_bp
from views.books import books_bp
from views.locations import location_bp
from views.stores import stores_bp
from views.transactions import transaction_bp
from views.payments import payments_bp
from db import mongo

app = Flask(__name__)
# CORS(app)
# app.config.from_object(config_class)
app.config["MONGO_URI"] = "mongodb://localhost:27017/lms"
CORS(app)

# Register blueprints here

app.register_blueprint(main_bp)
app.register_blueprint(authentication_bp, url_prefix='/auth')
# app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(location_bp, url_prefix='/locations')
app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(transaction_bp, url_prefix='/transactions')
app.register_blueprint(payments_bp, url_prefix='/payments')
app.register_blueprint(stores_bp, url_prefix='/stores')


@app.route('/test/')
def test_page():
    online_users = mongo.db.admin.find_one({"username": "admin"})
    o = json.loads(json_util.dumps(online_users))
    print(online_users)
    return {'users': o}


if __name__ == "__main__":
    app.run()
