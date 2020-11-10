from ArtifyAPI.settings.settings import DevConfig
from ArtifyAPI import app


def run(api):
    """ function Which start the API
    args:
        api (flask_restful.Api): builded API
    Returns:
        None
    """
    api.run()


if __name__ == "__main__":
    api = app.create_app(DevConfig)  # create application
    run(api)  # start application
