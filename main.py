from src import app_routes

from flask import Flask

app = Flask(__name__)

for route in app_routes:
    app.add_url_rule(**route)

if __name__ == '__main__':
    app.run(debug=True)