from backend import db
from backend.database import Admin
import bcrypt

salt = bcrypt.gensalt()

# new_admin  =  Admin(username = 'admin' , password =  bcrypt.hashpw('admin'.encode(), salt) )
# db.session.add(new_admin)
# db.session.commit()
# print(
#      Admin.query.first().password
    
# )
print(
    Admin.query.first()
    
)