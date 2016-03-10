from src.app import app

__author__ = 'edijemeni'

app.run(debug=app.config['DEBUG'], port=4990)