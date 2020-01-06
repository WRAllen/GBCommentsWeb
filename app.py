from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from GBComments import produceComments

 
app = Flask(__name__)
bootstrap = Bootstrap(app)
 
@app.route('/', methods=["GET", "POST"])
def main():
    comments = None
    _type = request.form.get("_type")
    _class = request.form.get("_class")
    if _type: comments = produceComments(_type, _class)
    return render_template('/main.html', comments=comments)
 
 
if __name__ == '__main__':
    app.run(debug=True)