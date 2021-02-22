from flask_migrate import Migrate, MigrateCommand

from flask_script import Manager
import app

def run(api):


    api.run(host="127.0.0.2")




if __name__ == "__main__":

    api = app.create_app()
    manager = Manager(api)
    migrate = Migrate(app, app.db)
    manager.add_command('db', MigrateCommand)
    run(api)






