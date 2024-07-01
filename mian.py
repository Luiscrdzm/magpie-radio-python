from flask import request, render_template as rt, Flask

app = Flask(__name__)


@app.route('/')
def index():
    return rt('index.html')



app.run()