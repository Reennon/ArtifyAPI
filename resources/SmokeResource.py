from flask_restful import Resource


class SmokeResorces(Resource):
    """
    GET endpoint hundler to test the process
    """

    def get(self):
        """

        Returns (str): Test message "Hello"
        """

        return 'Hello', 200

