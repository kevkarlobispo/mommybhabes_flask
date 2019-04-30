
# To create database on SQLLite

from flask_1.app_init import db
db.create_all()

from flask_1.models import User, Recipe
user_1 = User(username='kev_o',email='kevkarl.obispo@gmail.com',password='password')
db.session.add(user_1)
user_2 = User(username='john_o',email='jd@gmail.com',password='password')
db.session.add(user_2)
db.session.commit()

# Check Users
User.query.all()
User.query.first()
User.query.filter_by(username='kev_o').all()
User.query.filter_by(username='kev_o').first()
user = User.query.get(1) # parameter is ID


# Populating Packages
user = User.query.get(1)
package_1 = Package(title='Package 1', content='First Package Content!', user_id=user.id)
package_2 = Package(title='Package 2', content='Second Package Content!', user_id=user.id)
db.session.add(package_1)
db.session.add(package_2)
db.session.commit()

bootstrap

flask
rendering_template
url_for
flash
redirect
flask_wtf -> FlaskForm

SQLAlchemy


