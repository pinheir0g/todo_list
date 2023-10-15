from todo_list.db import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, default=None, index=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
        }
