from ArtifyAPI.settings.settings import DevConfig
from ArtifyAPI import app


def run(api):
    api.run()


if __name__ == "__main__":
    api = app.create_app(DevConfig)
    run(api)