from application import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    coursecode = db.Column(db.String(144), nullable=False)
    language = db.Column(db.String(144), nullable=False)
    level = db.Column(db.String(144), nullable=False)
    spots = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(144), nullable=False)
    registrationsopen = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, coursecode, language, level, spots, description, registrationsopen):
        self.name = name
        self.coursecode = coursecode
        self.language = language
        self.level = level
        self.spots = spots
        self.description = description
        self.registrationsopen = False
