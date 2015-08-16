from settings import APP_STATIC
from flask import Flask, render_template, send_from_directory
from app.controller import cv as cv_controller



app = Flask(__name__)



@app.route('/')
def show_about():
    return cv_controller.CVController().renderCVToHTML()

@app.route('/cv.pdf')
def get_pdf_cv():
    return send_from_directory(APP_STATIC, 'file/cv.pdf')

if __name__ == '__main__':
    app.run()