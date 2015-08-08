from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def show_about():
    return render_template('aboutme.html')

if __name__ == '__main__':
    app.run()