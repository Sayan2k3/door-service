import os
from flask import Flask, render_template

app = Flask(__name__)

from applications import config
from applications import models
from applications import routes

# @app.route('/')
# def index():
#     return render_template('prof.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
