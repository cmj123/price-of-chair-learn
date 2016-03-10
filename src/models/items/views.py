from flask import Blueprint

__author__ = 'edijemeni'

item_blueprint = Blueprint('items', __name__)

@item_blueprint.route('/item/<string:name>')
def item_page(name):
    pass

