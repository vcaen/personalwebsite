__author__ = 'vcaen'
import json
from app.settings import APP_CONTENT
from flask import render_template

class CVController:

    def renderCVToHTML(self):
        with open(APP_CONTENT + "/cv.json") as json_cv_file:
            json_cv = json.load(json_cv_file)

        return render_template('aboutme.html', cv=json_cv)
