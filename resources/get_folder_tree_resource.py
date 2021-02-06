import json
import os
import shutil
from http import HTTPStatus

from flask import request, flash, make_response, jsonify, render_template
from flask_login import current_user
from flask_restful import Resource

from app import db
from constants import Constants
from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from models.preference_file import Preference_file
from models.file import File
from utils.files import Files
from utils.utils import Utils
from utils.html_generate import GenerateHTML
import json

class GetFolderTreeResource(Resource):
    def get(self):
        if current_user.username == "user":
            return {
                "Cloud": {
                    "Preference_user_2": {
                        "3E": {}
                    }
                }
            }
        user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        curent_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,current_user_preference=True).first()
        user_preference_files = Preference_file.query.filter_by(preference_id = curent_preference.preference_id).all()
        paths=[]
        for file in user_preference_files:
            paths.append((File.query.filter_by(id=file.file_id).first()).file_name)
        tree = {}
        for item in paths:
            currTree = tree
            item=item.split('\\')
            for key in item[::]:
                if key not in currTree:
                    currTree[key] = {}
                currTree = currTree[key]
        html_code = GenerateHTML.generate_file_window_tree(tree)
        return html_code
