import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

# config
# TODO: development環境だけ？
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.environ.get('DATABASE_DB')

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
