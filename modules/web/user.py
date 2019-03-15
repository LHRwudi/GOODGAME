'''尽人事，听天命'''
from flask import Blueprint


user_blue = Blueprint('user_blue',import_name=__name__ , template_folder='../../templates')

@user_blue.route('/')
def user():
    return 'okuser'
