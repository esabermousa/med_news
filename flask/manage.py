from flask_script import Manager
from app import create_app

from app.core import  logger

# sets up the app
app = create_app()

manager = Manager(app)


@manager.command
def runserver():
    app.run(debug=True, host="0.0.0.0", port=5000)


@manager.command
def runworker():
    app.run(debug=False)
    

if __name__ == "__main__":
    manager.run()

    
    
    
