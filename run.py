from backend import app , db

db.create_all()
app.run(debug=True)