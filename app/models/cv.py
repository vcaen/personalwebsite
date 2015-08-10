__author__ = 'vcaen'


class Item(object):


    def __init__(self, title, short_desc, desc, picture):
        self.title = title
        self.short_desc = short_desc
        self.desc = desc
        self.picture = picture


class Work(Item):

    def __init__(self, title, short_desc, desc, date_begin, date_end, company, picture):
        super(Work, self).__init__(title, short_desc, desc, picture)
        self.date_begin = date_begin
        self.date_end = date_end
        self.company = company


class Project(Item):

    def __init__(self, title, short_desc, desc, picture, url):
        super(Project, self).__init__(title, short_desc, desc, picture)
        self.url = url


class Education(Item):

        def __init__(self, school, degree, picture, date_begin, date_end, title="", short_desc="", desc=""):
            super(Education, self).__init__(title, short_desc, desc, picture)
            self.school = school
            self.degree = degree
            self.date_begin = date_begin
            self.date_end = date_end



