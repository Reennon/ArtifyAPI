


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

    api.run(host="127.0.0.1", port=5000, debug=True)
