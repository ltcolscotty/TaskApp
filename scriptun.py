from api import app, db
from api import Todo


with app.app_context():
    db.create_all()
    todo = Todo(content='Test task')
    db.session.add(todo)
    db.session.commit()

    todo2 = Todo(content='test task 2')
    db.session.add(todo2)
    db.session.commit()