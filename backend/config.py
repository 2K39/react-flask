from backend import app
from uuid import uuid4

app.config["SECRET_KEY"] = uuid4().hex
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///files/database.db'