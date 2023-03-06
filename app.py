from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)

origins = ["http://localhost:3000", "localhost:3000", "http://127.0.0.1:3000", "http://127.0.0.1",
           "http://1292485-cc91283.tw1.ru", "http://1292485-cc91283.tw1.ru:3000",
           "http://www.1292485-cc91283.tw1.ru", "http://www.1292485-cc91283.tw1.ru:3000",
           "http://45.8.96.2", "http://45.8.96.2:3000"]

CORS(app, supports_credentials=True, resources={
    r"/*": {
        "origins": origins,
        "methods": ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
    },
})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app/todo.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Task(db.Model):
    """Model for tasks"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(120), default='')
    text = db.Column(db.String(500), nullable=False)
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.username}>'


@app.after_request
def after_request(response):
    """Options prerequest method"""
    response.headers.add('Access-Control-Allow-Origin', origins)
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Max-Age', '86400')
    return response


@app.route('/tasks', methods=['GET'])
def get_tasks():
    """View to get tasks"""
    with app.app_context():
        db.create_all()
        tasks = Task.query.all()
        return jsonify([
            {
                'id': task.id,
                'username': task.username,
                'email': task.email,
                'title': task.title,
                'text': task.text,
                'status': task.status
            } for task in tasks])


@app.route('/tasks', methods=['POST'])
def create_task():
    """View for creating tasks"""
    data = request.get_json()
    task = Task(username=data['username'], email=data['email'], title=data['title'], text=data['text'], status=False)
    db.session.add(task)
    db.session.commit()
    return {
        'id': task.id,
        'username': task.username,
        'email': task.email,
        'title': task.title,
        'text': task.text,
        'status': task.status
    }


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """View for deleting tasks"""
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return {
        'id': task.id,
        'username': task.username,
        'email': task.email,
        'title': task.title,
        'text': task.text,
        'status': task.status
    }


@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    """View for updating tasks"""
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.username = data.get('username', task.username)
    task.email = data.get('email', task.email)
    task.title = data.get('title', task.title)
    task.text = data.get('text', task.text)
    task.status = data.get('status', task.status)
    db.session.commit()
    return {
        'id': task.id,
        'username': task.username,
        'email': task.email,
        'title': task.title,
        'text': task.text,
        'status': task.status
    }


@app.route('/')
def hello_world():
    """Test view for main page"""
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
