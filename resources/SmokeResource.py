from flask_restful import Resource


class SmokeResorces(Resource):
    """
    GET endpoint hundler to test the process
    """

    def get(self):

        return 'Hello',200

