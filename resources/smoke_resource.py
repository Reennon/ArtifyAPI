from flask_restful import Resource


class SmokeResorces(Resource):
    """
    GET endpoint handler to test the process
    """

    def get(self):
        """
        send to core test message
        Returns (str): Test message "Hello"
        """
        """user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        current_preference = Curent_user_preference.query.filter_by(current_user_preference=True,
                                                                preference_user_id=user_preference_user.id).first()
        Files.update_db(current_user,current_preference)"""
        return {
            "Cloud": {
                "Preference_user_2": {
                    "3E": {
                        "Modules": {
                            "smoke_resource.py": {},
                            "Resources - Copy": {
                                "app.py": {},
                                "models.py": {}
                            },
                            "Scripts - Copy": {
                                "manege.py": {}
                            }
                        },
                        "Resources": {
                            "app.py": {},
                            "models.py": {}
                        },
                        "Scripts": {
                            "manege.py": {}
                        }
                    }
                }
            }
        }
