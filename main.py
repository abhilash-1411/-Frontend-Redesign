from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return "Welcome to the Flask!"

@app.route('/header')
def header():
    return render_template('header.html')

@app.route('/selectworkspace')
def selectworkspace():
    return render_template('selectworkspace.html')

@app.route('/footer')
def footer():
    return render_template('footer.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/createWorkspaceModal')
def createWorkspaceModal():
    return render_template('createWorkspaceModal.html')

@app.route('/toolbar')
def createWorkspaceProduct():
    return render_template('toolbar.html')

@app.route('/termsandcondition')
def termasAndConditions():
    return render_template('termsandconditionmodal.html')

@app.route('/workspaceProducts')
def workspaceProducts():
    return render_template('workspaceProducts.html')



if __name__ == '__main__':
    app.run(debug=True)
