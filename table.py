from os import environ 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), unique=True)

with app.app_context():
    db.create_all()  # Создаст таблицы, если их нет

@app.route("/", methods=['GET'])
def home():
    return 'Hello world!'

@app.route('/push', methods=['GET'])
def push():
    Url = request.args.get('url')
    print(Url)
    try:
        new_url = User(url=Url)
        print(new_url)
        db.session.add(new_url)
        db.session.commit()
        return {"status": "success", "message": "User added", "id": new_url.id}
    except Exception as e:
        db.session.rollback()
        return {"status": "error", "message": str(e)}

@app.route('/get', methods=['GET'])
def get_all_users():
    try:
        # Получаем всех пользователей из базы
        users = User.query.all()
        
        # Преобразуем в список словарей
        users_list = []
        for user in users:
            users_list.append({
                'id': user.id,
                'url': user.url
            })
        
        return {
            'status': 'success',
            'users': users_list,
            'count': len(users_list)
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

# docker run --name table --network=url-table-network -p 5000:4000 -e FLASK_ENV=development --add-host=db_host:172.17.0.2 --env-file .env -d table-app
# docker run --name mypostgres --network=url-table-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=mydb -p 5432:5432 -d postgres:13