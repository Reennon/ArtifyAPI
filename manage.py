

import app
from settings.settings import DevConfig
from constants import Constants

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
    api.run(host=Constants.HOST, port=4000, debug=True)

