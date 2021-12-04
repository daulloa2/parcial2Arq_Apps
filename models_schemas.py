
from flask import Flask,jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/apiatheoas2bim"
SQLALCHEMY_TRACK_MODIFICATIONS = False
ma = Marshmallow(app)



db= SQLAlchemy(app)

class Area(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50),nullable=False)
    contact_mail=db.Column(db.String(50),nullable=False)
    ext=db.Column(db.Integer,nullable=False)

class School(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50),nullable=False)
    capacity=db.Column(db.Integer,nullable=False)
    area_id=db.Column(db.Integer, db.ForeignKey('area.id'))
    area_= db.relationship('Area',backref='schoolof')


class Department(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50),nullable=False)
    telephone=db.Column(db.String(50),nullable=False)
    school_id=db.Column(db.Integer, db.ForeignKey('school.id'))
    school_= db.relationship('School',backref='deptof')


class Career(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50),nullable=False)
    acronym=db.Column(db.String(50),nullable=False,unique=True)
    department_id=db.Column(db.Integer, db.ForeignKey('department.id'))
    dept_= db.relationship('Department',backref='careerof')

class Course(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50),nullable=False)
    hours= db.Column(db.String(50), nullable=False)

    career_id=db.Column(db.Integer, db.ForeignKey('career.id'))
    career_= db.relationship('Career',backref='componentof') 

class Student(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(50), nullable=False,unique=True)
    name= db.Column(db.String(50),nullable=False)
    mail= db.Column(db.String(50), nullable=False,unique=True)

    course_id=db.Column(db.Integer, db.ForeignKey('course.id'))
    course_= db.relationship('Course',backref='classof')

#####################################################################################################
#                                          SCHEMAS                                                  #
#####################################################################################################

class AreaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'contact_mail','ext','_links')
        model=Area
               
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("get_Area", values=dict(id="<id>")),
            "area_collection": ma.URLFor("get_Areas"),
        }
    )

class SchoolSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'capacity','area_','_links')
        model=School
    area_ = ma.Nested(AreaSchema)             
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("get_School", values=dict(id="<id>")),
            "school_collection": ma.URLFor("get_Schools"),
        }
    )

class DepartmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'telephone','school_','_links')
        model=Department
    school_ = ma.Nested(SchoolSchema)             
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("get_Department", values=dict(id="<id>")),
            "dept_collection": ma.URLFor("get_Departments"),
        }
    )

class CareerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'acronym','dept_','_links')
        model=Career
    dept_ = ma.Nested(DepartmentSchema)     
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("get_Career", values=dict(id="<id>")),
            "career_collection": ma.URLFor("get_Careers"),
        }
    )

class CourseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'hours','career_','_links')
        model=Course
    career_ = ma.Nested(CareerSchema)  

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("get_Course", values=dict(id="<id>")),
            "course_collection": ma.URLFor("get_Courses"),
        }
    )

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'name', 'mail','course_','_links')
        model = Student

    course_ = ma.Nested(CourseSchema)
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("get_Student", values=dict(id="<id>")),
            "student_collection": ma.URLFor("get_Students"),
        }
    )

#db.drop_all()
db.create_all()