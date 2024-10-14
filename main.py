from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/header')
def header():
    return render_template('header.html')



if __name__ == '__main__':
    app.run(debug=True)
