from app.api import api
from flask import current_app

@api.route('/init', methods=['GET'])
def init():
    current_app.logger.debug("init called")
    return '', 204
