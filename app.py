from flask import Flask, render_template
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

# config
# TODO: development環境だけ？
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:""@localhost/hinagata-flask_development'

# database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# manager
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# routing
@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    manager.run()
