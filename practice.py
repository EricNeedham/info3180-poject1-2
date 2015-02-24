from app.models import User
from app import db
admin = User('admin','admin@example.com')
guest = User('guest','guest@example.com')
#addandcommitthenewuserstothedatabase
db.session.add(admin)
db.session.add(guest)
db.session.commit()