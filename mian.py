from flask import request, render_template, Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "En la granja de cepillin habia una vaca, una vaca, una vaca y una vaca."



app.run()