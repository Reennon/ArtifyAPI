from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

import app
from settings.settings import DevConfig


def run(api):
    """ function Which start the API
    args:
        api (flask_restful.Api): builded API
    Returns:
        None
    """

    api.run()


if __name__ == "__main__":
    api = app.create_app(DevConfig)
    manager = Manager(api)
    migrate = Migrate(app, app.db)
    manager.add_command('db', MigrateCommand)
    api.run(host="127.0.0.1", port=5000, debug=True)
