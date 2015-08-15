from flask import Flask, render_template
from app.controller import cv as cv_controller



app = Flask(__name__)



@app.route('/')
def show_about():
    return cv_controller.CVController().renderCVToHTML()

if __name__ == '__main__':
    app.run()