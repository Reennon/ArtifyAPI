from flask_restful import Resource
import app

class SmokeResorces(Resource):
    """
    GET endpoint handler to test the process
    """

    def get(self):

        student = {
            "id": 34,
            "group":'214',
            "firstname": "smfffoke",
            "lastname": "smodddke"
        }
        data = app.Student(student['id'] ,student['group'],student["firstname"],student["lastname"])
        app.db.session.add(data)
        app.db.session.commit()
        return 'Hello'

